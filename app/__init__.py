from flask import Flask
from config import config
from app import models
from app.extensions import db, csrf
from werkzeug.utils import find_modules, import_string


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.add_extension('jinja2.ext.do')

    # csrf.init_app(app)
    db.init_app(app)

    # register_blueprints(app, 'app.apis.auth')
    # register_blueprints(app, 'app.apis.test')
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # from .admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .apis.test import bp
    app.register_blueprint(bp, url_prefix='/test')

    return app


# def register_blueprints(app, package):
#     for module_name in find_modules(package):
#         module = import_string(module_name)
#         if hasattr(module, 'bp'):
#             bp = module.bp
#             app.register_blueprint(bp, url_prefix='/api/{0}'.format(bp.name))
