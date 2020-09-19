from flask import current_app
from app.extensions import db
from app.static import TOWN


class PenaltiesRule(db.Model):
    """
        记录每个不同的小区获取的扣分规则
    """
    __tablename__ = 'penalties_rule'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))  # 扣分名称
    desc = db.Column(db.String(256))  # 具体扣分的说明
    item_name = db.Column(db.String(1024))  # 打分项
    street_id = db.Column(db.String(8))  # 属于的街道

    def commit_(obj: object):
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            current_app.logger.error('Pictures insert error:%s' % str(e))

    @staticmethod
    def findRegionIdByName(name):
        regionName = name.strip().lower()
        if regionName in [
                "塔山街道", "府山街道", "北海街道", "城南街道", "稽山街道", "迪荡街道", "灵芝街道"
        ]:
            return 1
        elif regionName in [
                "皋埠街道", "陶堰街道", "富盛镇", "马山街道", "孙端街道", "东湖街道", "东浦街道", "鉴湖街道",
                "斗门街道", "沥海街道"
        ]:
            return 2

    @staticmethod
    def findItemByStreetAndHouse(name, houseName):
        """
            1 为城区  2 为城镇
        """
        name = name.strip().lower()
        houseName = houseName.strip().lower()
        if name in ["塔山街道", "府山街道", "北海街道", "城南街道", "稽山街道", "迪荡街道", "灵芝街道"
                    ] and f"{name}_{houseName}" not in TOWN:
            return 1
        return 2

    @staticmethod
    def findItemByStreetName(name, houseName):
        base = ["基础工作", "项目保障", "宣传工作", "垃圾分类收集容器设置", "队伍建设", "分类投放", "分类收运"]
        if PenaltiesRule.findItemByStreetAndHouse(name, houseName) == 1:
            return base + ["集置点管理"]
        return base + ["处置(中转)场所管理"]

    @classmethod
    def insert_(cls, street_id, desc, item_name, name):
        dt = {
            "name": name,
            "desc": desc,
            "item_name": item_name,
            "street_id": street_id,
        }
        penalties_rule = PenaltiesRule(**dt)
        cls.commit_(penalties_rule)

    def to_dict(self):
        return {
            "id": self.id,
            "desc": self.desc,
            "ruleName": self.name,
            "itemName": self.item_name,
            "regionId": self.street_id,
        }
