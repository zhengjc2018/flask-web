"""
    用于获取报表
"""
import os
from flask import Blueprint, request, jsonify, app, current_app, send_file, send_from_directory, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required
from app.models import Users, History
from .response import newResponse


bp = Blueprint('report', __name__)
api = Api(bp)


# 获取报表以及台账内容
@api.resource('/getReport')
class getReportResource(Resource):

    @jwt_required
    def get(self):
        page_size = int(request.args.get("pageSize", 10))
        page_no = int(request.args.get("pageNo", 1))
        type_ = int(request.args.get('type', 1))
        history = History.query.filter_by(type_=type_).paginate(page_no, page_size, True)
        result = [i.to_dict() for i in history.item]
        return newResponse(result, 200, "success")


@api.resource('/downloadReport')
class downloadReportResource(Resource):
    # 下载报表
    @jwt_required
    def get(self):
        file_name = request.args.get("fileName", "test.docx")
        base_dir = current_app.config['RAW_REPORT_FOLDER']

        response = make_response(send_from_directory(base_dir, file_name, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
        return response
