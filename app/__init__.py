from flask import Flask
from config import config
from app import models
from app.extensions import db, jwt, celery
from celery_once import QueueOnce
from werkzeug.utils import find_modules, import_string


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py', silent=True)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.add_extension('jinja2.ext.do')

    register_blueprints(app, 'app.api.v1')
    _init_extensions(app)
    return app


def _init_extensions(app):
    celery.init_app(app)

    class ContextQueueOnce(QueueOnce):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super(ContextQueueOnce, self).__call__(*args, **kwargs)
    celery.QueueOnce = ContextQueueOnce
    db.init_app(app)
    jwt.init_app(app)


def register_blueprints(app, package):
    for module_name in find_modules(package):
        module = import_string(module_name)
        if hasattr(module, 'bp'):
            bp = module.bp
            app.register_blueprint(bp, url_prefix='/api/{0}'.format(bp.name))
