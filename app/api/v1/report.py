"""
    用于获取报表
"""
import os
from time import time
from flask import Blueprint, request, jsonify, app, current_app, send_file, send_from_directory, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required
from app.models import Users, History
from app.commons import make_zip
from .response import newResponse
from urllib import parse
import logging
import shutil


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
        file_name = parse.unquote(request.args.get("fileName", ""))
        base_dir = current_app.config['RAW_REPORT_FOLDER']
        file_name = os.path.join(base_dir, file_name)

        from_ = request.args.get("from")
        to_ = request.args.get("to")

        if from_ and to_:
            zip_dir_name = time() * 1000
            history = History.query.filter(History.gmt_create>= from_, History.gmt_create<=to_).all()
            template_dir = os.path.join(base_dir, str(zip_dir_name))
            for i in history:
                try:
                    shutil.copy(i.file_name, template_dir)
                except Exception as e:
                    print(f"copy file error: {str(e)}")
            make_zip(template_dir, f"{zip_dir_name}.zip")
            shutil.rmtree(template_dir)
            file_name = f"{zip_dir_name}.zip"

        response = make_response(send_file(file_name))
        basename = os.path.basename(file_name)
        response.headers["Content-Disposition"] = \
            "attachment;" \
            "filename*=UTF-8''{utf_filename}".format(
                utf_filename=parse.quote(basename.encode('utf-8'))
        )
        return response
