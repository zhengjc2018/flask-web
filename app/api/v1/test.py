from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from app.tasks import start_test


bp = Blueprint('test', __name__)
api = Api(bp)


@api.resource('/privew')
class Testdasdas(Resource):

    def get(self):
        return "hello world get"

    def post(self):
        return start_test.delay()


if __name__ == "__main__":
    print(generate_password_hash("super"))
