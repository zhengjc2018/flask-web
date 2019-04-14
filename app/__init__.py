from flask import Flask
from config import config
from werkzeug.utils import find_modules, import_string


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    print(config[config_name], '\n'*5)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)

    register_blueprints(app, 'app.apis')
    return app


def register_blueprints(app, package):
    for module_name in find_modules(package):
        module = import_string(module_name)
        if hasattr(module, 'bp'):
            bp = module.bp
            app.register_blueprint(bp, url_prefix='/api/{0}'.format(bp.name))
