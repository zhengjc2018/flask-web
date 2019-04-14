import os

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
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379'

    CELERYBEAT_SCHEDULE = {
        # use to auto inspect
        # 't1': {
        #     'task': 'add_together',
        #     'schedule': timedelta(seconds=3)
        # },
        # 'auto_job': {
        #     'task': 'auto_job_trigger',
        #     'schedule': crontab(minute='*/15')
        # },
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
    #     'mysql+pymysql://root:zjc@localhost/zjc_test?charset=utf8'
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 120
    SQLALCHEMY_POOL_TIMEOUT = 20


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
