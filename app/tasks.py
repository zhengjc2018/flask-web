from flask import current_app
from app.extensions import celery


@celery.task(name='start_fetchlog')
def start_fetchlog():
    print("celery test")
