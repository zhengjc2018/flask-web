from flask import current_app
from app.extensions import db


class Houses(db.Model):
    __tablename__ = 'houses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    street_id = db.Column(db.Integer)
    community_id = db.Column(db.Integer)

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Houses insert error:%s' % str(e))

    @classmethod
    def insert_(cls, name, street_id, community_id):
        dt = {
            "name": name,
            "street_id": street_id,
            "community_id": community_id,
        }
        houses = Houses(**dt)
        cls.commit_(houses)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "street_id": self.street_id,
            "community_id": self.community_id,
        }
