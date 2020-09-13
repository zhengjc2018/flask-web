from flask import current_app
from app.extensions import db


class Streets(db.Model):
    __tablename__ = 'streets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Streets insert error:%s' % str(e))

    @classmethod
    def insert_(cls, name):
        dt = {
            "name": name,
        }
        streets = Streets(**dt)
        cls.commit_(streets)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def findIdByName(name):
        street = Streets.query.filter_by(name=name.strip()).first()
        if street:
            return True, street.id
        return False, None
