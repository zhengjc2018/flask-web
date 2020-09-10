"""
    用于登录验证以及增删查用户
"""
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required
from app.models import Users
from .response import newResponse


bp = Blueprint('user', __name__)
api = Api(bp)


@api.resource('/Login')
class LoginResource(Resource):

    def post(self):
        data = request.json
        login_name = data.get("login_name")
        login_pass = data.get("login_pass")

        user = Users.query.filter_by(login_name=login_name).first()
        token = create_access_token(identity=user.to_dict())
        if not user or not user.check_login_pass(login_pass):
            return newResponse("", 400, "passwd or username not valiade")
        return newResponse(token, 200)


@api.resource('/CreateUser')
class CreateUserResource(Resource):

    @jwt_required
    def post(self):
        data = request.json
        login_name = data.get("login_name")
        login_pass = data.get("login_pass")
        desc = data.get('desc')

        Users.insert_(login_name, login_pass, desc)
        return newResponse("", 200)


@api.resource('/DeleteUser')
class DeleteUserResource(Resource):

    @jwt_required
    def post(self):
        data = request.json
        login_name = data.get("login_name")

        Users.query.filter_by(login_name=login_name).delete()
        return newResponse("", 200)


@api.resource('/ListUsers')
class ListUsersResource(Resource):

    @jwt_required
    def get(self):
        data = [i.to_dict() for i in Users.query.all()]
        return newResponse(data, 200)
