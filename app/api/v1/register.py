"""
    用于采集扣分信息
"""
import os
from flask import Blueprint, request, current_app
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required

from app.models import Marks, Pictures, PenaltiesRule
from app.static import STREETS
from .response import newResponse


bp = Blueprint('register', __name__)
api = Api(bp)


@api.resource('/upload')
class RegisterResource(Resource):

    @jwt_required
    def post(self):
        """
            item为扣分规则， value为扣的分值, user为登录用户名, area 为打分的地区

            {
                'data': [{'itemId': 1, 'value': 1, 'fileName': ['xxx']} .....]
                'user': xxxxx,
                'area': 'xxx',
            }
        """
        data = request.json
        marks = data.get("data")
        user_name = data.get('user')
        dirName = os.path.join(current_app.config['RAW_PICTURE_FOLDER'],
                               Marks.get_picture_dir_name(user_name))
        upload_files = request.files.getlist('file')
        for file in upload_files:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(dirName, filename)
            file.save(upload_path)

        for i in marks:
            Pictures.insert_(
                i.get("value"), i.get('fileName'), i.get('itemId'))

        # todo  own_by设计
        own_by = 1
        Marks.insert_(own_by, user_name, dirName)
        return newResponse("", 200)


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
        name = request.args.get("regionName")
        itemName = request.args.get("itemName")

        penaltiesRule = PenaltiesRule.query.filter_by(
            itemName=itemName,
            regionId=PenaltiesRule.findRegionIdByName(name)).all()

        data = [i.to_dict() for i in penaltiesRule]
        return newResponse(data, 200)


# 获取所有的街道
@api.resource('/getStreets')
class GetStreetsResource(Resource):
    @jwt_required
    def get(self):
        result = dict()
        for key, value in STREETS.items():
            result[key] = value
        return newResponse(result, 200)


# 获取对应街道下的所有小区
@api.resource('/getHouses')
class GetHousesResource(Resource):
    @jwt_required
    def get(self):
        result = dict()
        for key, value in STREETS.items():
            result[key] = value
        return newResponse(result, 200)
