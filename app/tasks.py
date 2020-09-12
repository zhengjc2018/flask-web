from flask import current_app
from app.extensions import celery


@celery.task(name='start_test')
def start_test():
    print("celery test")
