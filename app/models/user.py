from flask import current_app
from app.extensions import db
from app.commons import TimesUnit
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(64), unique=True)
    login_pass = db.Column(db.String(256))
    desc = db.Column(db.String(256))
    update_at = db.Column(db.Integer)

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Users insert error:%s' % str(e))

    @classmethod
    def insert_(cls, name, pwd, desc=""):
        dt = {
            "login_name": name,
            "login_pass": pwd,
            "update_at": TimesUnit.get_now(),
            "desc": desc,
        }
        user = Users(**dt)
        cls.commit_(user)

    def check_login_pass(self, password):
        return check_password_hash(self.login_pass, password)

    def to_dict(self):
        return {
            "login_name": self.login_name,
            "desc": self.desc,
            "update_at": self.update_at
        }
