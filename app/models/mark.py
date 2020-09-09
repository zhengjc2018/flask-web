from flask import current_app
from app.extensions import db
from app.commons import TimesUnit


class Marks(db.Model):
    __tablename__ = 'marks'
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer)
    own_by = db.Column(db.Integer)   # 属于哪个小区或者县区
    user_name = db.Column(db.String(256), unique=True)
    gmt_create = db.Column(db.Integer)
    picture_num = db.Column(db.Integer)
    picture_path = db.Column(db.String(256))   # 用于记录照片存放的地址

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Marks insert error:%s' % str(e))

    @classmethod
    def insert_(cls, mark, own_by, user_name, picture_num, picture_path):
        dt = {
            "mark": mark,
            "own_by": own_by,
            "gmt_create": TimesUnit.get_now(),
            "user_name": user_name,
            "picture_num": picture_num,
            "picture_path": picture_path
        }
        mark = Marks(**dt)
        cls.commit(mark)

    def to_dict(self):
        return {
            "mark": self.mark,
            "own_by": self.own_by,
            "gmt_create": self.gmt_create,
            "user_name": self.user_name,
            "picture_num": self.picture_num,
            "picture_path": self.picture_path,
            "id": self.id,
        }

    @staticmethod
    def get_picture_dir_name(user_name):
        return "{0}_{1}".format(user_name, TimesUnit.get_now())
