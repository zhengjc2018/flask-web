from flask import current_app
from app.extensions import db
from app.commons import TimesUnit


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(512))                      # 文件名
    gmt_create = db.Column(db.Integer)
    type_ = db.Column(db.Integer)                             # 用于区分是报表还是台账内容  1 为报表， 2为台账
    street_name = db.Column(db.String(128))                    # 所属街道名
    others = db.Column(db.String(128), default="")

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('History insert error:%s' % str(e))

    @classmethod
    def insert_(cls, file_name, type_, street_name):
        dt = {
            "file_name": file_name,
            "type_": type_,
            "gmt_create": TimesUnit.get_now(),
            "street_name": street_name,
        }
        history = History(**dt)
        cls.commit_(history)

    def to_dict(self):
        return {
            "id": self.id,
            "fileName": self.file_name,
            "type_": self.type_,
            "gmtCreate": self.gmt_create,
            "streetName": self.street_name,
            "others": self.others,
        }
