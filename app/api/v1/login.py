"""
    用于登录验证以及增删查用户
"""
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

from app.models import Users


bp = Blueprint('user', __name__)
api = Api(bp)


@api.resource('/Login')
class LoginResource(Resource):

    def post(self):
        data = request.json
        login_name = data.get("login_name")
        login_pass = data.get("login_pass")

        user = Users.query.filter_by(login_name=login_name).first()
        if not user or not user.check_password(login_pass):
            return False
        return True


@api.resource('/CreateUser')
class CreateUserResource(Resource):

    def post(self):
        data = request.json
        login_name = data.get("login_name")
        login_pass = data.get("login_pass")
        desc = data.get('desc')

        Users.insert_(login_name, login_pass, desc)
        return True


@api.resource('/DeleteUser')
class DeleteUserResource(Resource):

    def post(self):
        data = request.json
        login_name = data.get("login_name")

        Users.query.filter_by(login_name=login_name).delete()
        return True


@api.resource('/ListUsers')
class ListUsersResource(Resource):

    def get(self):
        data = [i.to_dict() for i in Users.query.all()]
        return data
