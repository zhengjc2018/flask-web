"""
    用于采集扣分信息
"""
import os
import json
from flask import Blueprint, request, current_app
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required

from app.models import PenaltiesRule, Plan
from app.static import STREETS, HOUSES, ITEM_RULE
from .response import newResponse
import uuid


bp = Blueprint('register', __name__)
api = Api(bp)


# 数据中心展示
@api.resource('/list')
class RegisterListResource(Resource):
    @jwt_required
    def get(self):
        data = list()
        basePath = current_app.config['RAW_HISTORY_FOLDER']
        for root, _, files in os.walk(basePath):
            for file in files:
                if os.path.isdir(file):
                    continue
                data.append({"file": file, "path": os.path.join(root, file)})

        return newResponse(data, 200)


# 获取扣分标准
@api.resource('/getRule')
class GetRuleResource(Resource):
    @jwt_required
    def get(self):
        streetName = request.args.get("streetName")
        houseName = request.args.get("houseName")

        result = dict()
        type_ = PenaltiesRule.findItemByStreetAndHouse(streetName, houseName)

        for (t, desc, item, rule) in ITEM_RULE:
            if t != type_:
                continue
            if result.get(item):
                result[item].append(rule)
            else:
                result[item] = [rule]

        return newResponse(result, 200)


# 根据街道名来获取打分项
@api.resource('/getItems')
class GetItemsResource(Resource):
    @jwt_required
    def get(self):
        streetName = request.args.get("streetName")
        houseName = request.args.get("houseName")
        data = PenaltiesRule.findItemByStreetName(streetName, houseName)
        return newResponse(data, 200)


# 获取所有的街道
@api.resource('/getStreets')
class GetStreetsResource(Resource):
    @jwt_required
    def get(self):
        result = dict()
        for key, value in STREETS.items():
            result[value] = key
        return newResponse(result, 200)


# 获取对应街道下的所有小区
@api.resource('/getHouses')
class GetHousesResource(Resource):
    @jwt_required
    def get(self):
        result = list()
        street_id = request.args.get("streetId")
        for i in HOUSES.get(street_id):
            result.append(i[0])

        return newResponse(result, 200)


@api.resource('/upload')
class UploadResource(Resource):
    @jwt_required
    def post(self):
        dirName = current_app.config['RAW_PICTURE_FOLDER']
        if not os.path.exists(dirName):
            os.mkdir(dirName)

        file = request.files.get('file')
        path = os.path.join(dirName, f"{str(uuid.uuid4())}.jpeg")
        file.save(path)
        return path


@api.resource('/planDetail')
class PlanResource(Resource):
    @jwt_required
    def get(self):
        planId = int(request.args.get("planId"))
        plan = Plan.query.get(planId)
        data = json.loads(plan.content)
        result = {
            "data": data,
            "streetName": STREETS.get(str(plan.street_id)),
            "houseName": plan.house_name
        }
        return newResponse(result, 200)

    @jwt_required
    def post(self):
        data = request.json
        marks = data.get("data")
        plan_name = data.get('planName')
        user_name = data.get('userName')
        street_id = data.get('streetId')
        house_name = data.get('houseName')

        Plan.insert_(user_name, json.dumps(marks), street_id, house_name, plan_name)
        return newResponse("", 200)


# 列出某个用户下的所有计划
@api.resource('/listPlans')
class ListPlansResource(Resource):
    # @jwt_required
    def get(self):
        userName = request.args.get("userName")
        page_size = int(request.args.get("pageSize", 10))
        page_no = int(request.args.get("pageNo", 1))
        queryObj = Plan.query.filter_by(user_name=userName).order_by(Plan.update_at.desc())
        plan = queryObj.paginate(page_no, page_size, True)

        result = {
            "totalCount": len(queryObj.all()),
            "data": [i.to_simple_dict() for i in plan.items]
        }
        return newResponse(result, 200, "")
