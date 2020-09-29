"""
    用于获取报表
"""
import os
from flask import Blueprint, request, jsonify, app, current_app, send_file, send_from_directory, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required
from app.models import Users, History
from .response import newResponse
from urllib import parse


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

        queryObj = History.query.filter_by(type_=type_).order_by(History.gmt_create.desc())
        history = queryObj.paginate(page_no, page_size, True)

        data = []
        for plan in history.items:
            data.append({
                "id": plan.id,
                "fileName": os.path.split(plan.file_name)[1],
                "type_": plan.type_,
                "gmtCreate": plan.gmt_create,
                "streetName": plan.street_name,
                "others": plan.others,
            })

        result = {
            "totalCount": len(queryObj.all()),
            "data": data
        }

        return newResponse(result, 200, "success")


@api.resource('/downloadReport')
class downloadReportResource(Resource):
    # 下载报表
    # @jwt_required
    def get(self):
        file_name = parse.unquote(request.args.get("fileName", "test.docx"))
        base_dir = current_app.config['RAW_REPORT_FOLDER']

        response = make_response(send_from_directory(base_dir, file_name, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
        return response
