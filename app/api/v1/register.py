"""
    用于采集扣分信息
"""
import os
from flask import Blueprint, request, jsonify, current_app
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
from app.commons import TimesUnit

from app.models import Marks


bp = Blueprint('register', __name__)
api = Api(bp)


@api.resource('/Upload')
class RegisterResource(Resource):

    def post(self):
        data = request.json

        mark = data.get("mark")
        user_name = data.get('userName')
        dirName = os.path.join(current_app.config['RAW_PICTURE_FOLDER'],
                               Marks.get_picture_dir_name(user_name))
        upload_files = request.files.getlist('file')
        for file in upload_files:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(dirName, filename)
            file.save(upload_path)

        # todo  own_by设计
        Marks.insert_(mark, 1, user_name, len(upload_files), dirName)
        return True


# 数据中心展示
@api.resource('/Upload')
class RegisterResource(Resource):

    def post(self):
        data = request.json

        mark = data.get("mark")
        user_name = data.get('userName')
        dirName = os.path.join(current_app.config['RAW_PICTURE_FOLDER'],
                               Marks.get_picture_dir_name(user_name))
        upload_files = request.files.getlist('file')
        for file in upload_files:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(dirName, filename)
            file.save(upload_path)

        # todo  own_by设计
        Marks.insert_(mark, 1, user_name, len(upload_files), dirName)
        return True
