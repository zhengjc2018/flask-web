from flask import current_app
from app.extensions import db
from app.commons import TimesUnit


class Pictures(db.Model):
    """
        记录图片的位置以及属于哪个小区，扣分情况
    """
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.Integer)                       # 判断扣分规则是哪个
    mark = db.Column(db.Float)                         # 分值
    gmt_create = db.Column(db.Integer)
    picture_name = db.Column(db.String(256))

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Pictures insert error:%s' % str(e))

    @classmethod
    def insert_(cls, mark, picture_name, type_):
        dt = {
            "mark": mark,
            "type_": type_,
            "gmt_create": TimesUnit.get_now(),
            "picture_name": picture_name,
        }
        picture = Pictures(**dt)
        cls.commit_(picture)

    def to_dict(self):
        return {
            "id": self.id,
            "mark": self.mark,
            "type_": self.type_,
            "gmt_create": self.gmt_create,
            "picture_name": self.picture_name,
        }
