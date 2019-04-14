from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource


bp = Blueprint('test', __name__)
api = Api(bp)


@api.resource('/privew')
class Testdasdas(Resource):

    def get(self):
        return "hello world get"

    def post(self):
        return "hello world post"
