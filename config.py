import os
from celery.schedules import crontab, timedelta


base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    SECRET_KEY = 'hard to guess string'
    # RESTFUL SETTING
    ERROR_404_HELP = False
    # SQLALCHEMY SETTING
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CELERY SETTING
    CELERYD_TASK_SOFT_TIME_LIMIT = 2000
    CELERY_DISABLE_RATE_LIMITS = True
    CELERYD_FORCE_EXECV = True
    CELERYD_MAX_TASKS_PER_CHILD = 30
    CELERY_DISABLE_RATE_LIMITS = True
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_BROKER_URL = 'redis://localhost:6379/10'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/11'

    RAW_PICTURE_FOLDER = os.path.join(base_dir, 'app', 'static', 'picture')
    RAW_HISTORY_FOLDER = os.path.join(base_dir, 'app', 'static', 'history')
    RAW_REPORT_FOLDER = os.path.join(base_dir, 'app', 'static', 'report')   # 用于生成excel报表

    CELERYBEAT_SCHEDULE = {
        # use to auto inspect
        # 't1': {
        #     'task': 'add_together',
        #     'schedule': timedelta(seconds=3)
        # },
        'generate_excel_city': {
            'task': 'generate_excel_city',
            'schedule': crontab(day_of_month=29, hour=23, minute=0),
            "args": (),
        },
        'generate_excel_town': {
            'task': 'generate_excel_town',
            'schedule': crontab(day_of_month=29, hour=23, minute=0),
            "args": (),
        },
        'generate_assessment_form': {
            'task': 'generate_assessment_form',
            'schedule': crontab(minute=0, hour=20, day_of_week='mon,wed'),
            "args": (),
        },
        'generate_assessment_form_for_month': {
            'task': 'generate_assessment_form_for_month',
            'schedule': crontab(day_of_month=29, hour=23, minute=0),
            "args": (),
        },
        'generate_assessment_total': {
            'task': 'generate_assessment_total',
            'schedule': crontab(day_of_month=29, hour=23, minute=0),
            "args": (),
        },
    }
    # ONCE = {
    #     'backend': 'celery_once.backends.Redis',
    #     'settings': {
    #         'url': 'redis://localhost:6379/10',
    #         'default_timeout': 6 * 60 * 60
    #     }
    # }


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY SETTING
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(base_dir, 'dev.sqlite')
    # SQLALCHEMY_DATABASE_URI = \
    #     'mysql+pymysql://root:zjc@localhost/geass'

    # SQLALCHEMY_POOL_SIZE = 100
    # SQLALCHEMY_POOL_RECYCLE = 120
    # SQLALCHEMY_POOL_TIMEOUT = 20


class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = 'okp'
    # SQLALCHEMY SETTING
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
