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
import logging


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
        query = request.args.get("query")

        if query:
            queryObj = History.query.filter(History.type_ == type_, History.file_name.like(f"%{query}%")).order_by(History.gmt_create.desc())
        else:
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
        file_name = parse.unquote(request.args.get("fileName"))
        base_dir = current_app.config['RAW_REPORT_FOLDER']
        # logging.info(f"filename: {file_name}\n\n")
        # # response = make_response(send_from_directory(base_dir, parse.quote(file_name.encode('utf-8').decode('utf-8')), as_attachment=True))
        # # response.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
        # # return response

        # response = make_response(send_from_directory(base_dir, file_name, as_attachment=True, conditional=True))
        # response.headers["Content-Disposition"] = 'attachment; filename={}"'.format(parse.quote(file_name))
        # return response
        file_name = os.path.join(base_dir, file_name)
        response = make_response(send_file(file_name))
        basename = os.path.basename(file_name)
        response.headers["Content-Disposition"] = \
            "attachment;" \
            "filename*=UTF-8''{utf_filename}".format(
                utf_filename=parse.quote(basename.encode('utf-8'))
        )
        return response
