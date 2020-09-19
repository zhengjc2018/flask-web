from flask import current_app
from app.extensions import db


class Houses(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)    # 1 为城区 2为城镇
    name = db.Column(db.String(256))
    street_id = db.Column(db.String(16))
    community_name = db.Column(db.String(256))

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Houses insert error:%s' % str(e))

    @classmethod
    def insert_(cls, name, street_id, community_name, type):
        dt = {
            "name": name,
            "type": type,
            "street_id": street_id,
            "community_name": community_name,
        }
        houses = Houses(**dt)
        cls.commit_(houses)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "street_id": self.street_id,
            "community_name": self.community_name,
        }
