from flask import current_app
from app.extensions import db


class PenaltiesRule(db.Model):
    """
        记录每个不同的小区获取的扣分规则
    """
    __tablename__ = 'penalties_rule'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))             # 扣分名称
    desc = db.Column(db.String(256))             # 具体扣分的说明
    itemName = db.Column(db.String(256))         # 打分项
    regionId = db.Column(db.Integer)             # 属于的街道

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Pictures insert error:%s' % str(e))

    @staticmethod
    def findRegionIdByName(name):
        regionName = name.strip().lower()
        if regionName in ["塔山街道", "府山街道", "北海街道", "城南街道", "稽山街道", "迪荡街道", "灵芝街道"]:
            return 1
        elif regionName in ["皋埠街道", "陶堰街道", "富盛镇", "马山街道", "孙端街道", "东湖街道", "东浦街道", "鉴湖街道", "斗门街道", "沥海街道"]:
            return 2

    @classmethod
    def insert_(cls, regionId, desc, itemName, name):
        dt = {
            "name": name,
            "desc": desc,
            "itemName": itemName,
            "regionId": regionId,
        }
        penalties_rule = PenaltiesRule(**dt)
        cls.commit_(penalties_rule)

    def to_dict(self):
        return {
            "id": self.id,
            "desc": self.desc,
            "name": self.name,
            "itemName": self.itemName,
            "regionId": self.regionId,
        }
