from flask import Blueprint, request, jsonify
import json
from datetime import datetime
from app.commons import ExcelUtils, TimesUnit
from app.static import HOUSES, STREETS
from app.models import Plan
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from app.tasks import start_test
from xlutils.copy import copy
import xlrd
from app.tasks import generate_excel_city, generate_excel_town, generate_assessment_form

bp = Blueprint('test', __name__)
api = Api(bp)


@api.resource('/privew')
class Testdasdas(Resource):
    def get(self):
        return "hello world get"

    def post(self):
        generate_assessment_form()



if __name__ == "__main__":
    print(generate_password_hash("super"))
