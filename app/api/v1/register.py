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
from app.static import STREETS, HOUSES
from .response import newResponse


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
    # @jwt_required
    def get(self):
        streetId = request.args.get("streetId")
        itemName = request.args.get("itemName")

        penaltiesRule = PenaltiesRule.query.filter_by(
            itemName=itemName,
            regionId=streetId).all()

        data = [i.to_dict() for i in penaltiesRule]
        return newResponse(data, 200)


# 根据街道名来获取打分项
@api.resource('/getItems')
class GetItemsResource(Resource):
    # @jwt_required
    def get(self):
        streetName = request.args.get("streetName")
        data = PenaltiesRule.findItemByStreetName(streetName)
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


@api.resource('/planDetail')
class PlanResource(Resource):
    # @jwt_required
    def get(self):
        planId = int(request.args.get("planId"))
        plan = Plan.query.get(planId)
        data = json.loads(plan.content)
        return newResponse(data, 200)

    # @jwt_required
    def post(self):
        data = request.json
        marks = data.get("data")
        user_name = data.get('userName')
        street_id = data.get('streetId')
        house_name = data.get('houseName')

        dirName = os.path.join(current_app.config['RAW_PICTURE_FOLDER'],
                               Plan.get_picture_dir_name(user_name))
        if not os.path.exists(dirName):
            os.mkdir(dirName)

        upload_files = request.files.getlist('file')
        for file in upload_files:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(dirName, filename)
            file.save(upload_path)

        for i in marks:
            i["fileName"] = [os.path.join(dirName, i) for i in i.get("fileName")]

        Plan.insert_(user_name, json.dumps(marks), street_id, house_name)
        return newResponse("", 200)


# 列出某个用户下的所有计划
@api.resource('/listPlans')
class ListPlansResource(Resource):
    # @jwt_required
    def get(self):
        userName = request.args.get("userName")
        plan = Plan.query.filter_by(user_name=userName).all()
        result = [i.id for i in plan]

        return newResponse(result, 200)
