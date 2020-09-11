# from flask import current_app
# from app.extensions import db
# from app.commons import TimesUnit


# class History(db.Model):
#     __tablename__ = 'history'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Integer)                      # 属于哪个小区或者县区
#     user_name = db.Column(db.String(256), unique=True)
#     gmt_create = db.Column(db.Integer)
#     picture_id = db.Column(db.Integer)                  # 用于扣分规则
#     picture_path = db.Column(db.String(256))            # 用于记录照片存放的地址

#     def commit_(obj: object):
#         try:
#             db.session.add(obj)
#             db.session.commit()
#         except Exception as e:
#             current_app.logger.error('Marks insert error:%s' % str(e))

#     @classmethod
#     def insert_(cls, own_by, user_name, picture_path):
#         dt = {
#             "own_by": own_by,
#             "user_name": user_name,
#             "gmt_create": TimesUnit.get_now(),
#             "picture_path": picture_path,
#         }
#         mark = Marks(**dt)
#         cls.commit(mark)

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "own_by": self.own_by,
#             "user_name": self.user_name,
#             "gmt_create": self.gmt_create,
#             "picture_path": self.picture_path,
#         }
