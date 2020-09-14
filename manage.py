import os
import random
from app import create_app, db, celery
from app.models import Users, PenaltiesRule, Houses
from app.static import ITEM_RULE, STREETS, HOUSES
from app.commons import TimesUnit
from flask import jsonify, request
from werkzeug.security import generate_password_hash
from flasgger import Swagger, swag_from


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
celery = celery
Swagger(app)


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, db=db)
    return context


@app.cli.command("init_db")
def init_db():
    # 初始化登录管理员
    Users.insert_("super", generate_password_hash("super"), "superUser")

    # 初始化扣分规则
    for i in ITEM_RULE:
        PenaltiesRule.insert_(*i)

    # 初始化小区
    for k, v in HOUSES.items():
        ho, comm = v
        Houses.insert_(ho, k, comm)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
