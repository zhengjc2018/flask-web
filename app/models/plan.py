from flask import current_app
from app.extensions import db
from app.commons import TimesUnit
from werkzeug.security import generate_password_hash, check_password_hash


class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64))
    content = db.Column(db.Text)
    update_at = db.Column(db.Integer)
    street_id = db.Column(db.String(8))
    house_name = db.Column(db.String(64))

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Plan insert error:%s' % str(e))

    @classmethod
    def insert_(cls, user_name, content, street_id, house_name):
        dt = {
            "content": content,
            "user_name": user_name,
            "street_id": street_id,
            "house_name": house_name,
            "update_at": TimesUnit.get_now(),
        }
        plan = Plan(**dt)
        cls.commit_(plan)

    @staticmethod
    def get_picture_dir_name(name):
        return f"{name}_{TimesUnit.get_now()}"

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "userName": self.user_name,
            "updateAt": self.update_at,
            "streetId": self.street_id,
            "houseName": self.house_name,
        }
