from flask import current_app
import json
from app.extensions import celery
from datetime import datetime
from app.commons import ExcelUtils, WordUtils, TimesUnit
from app.models import Plan
from app.static import STREETS, HOUSES


@celery.task(name='start_test')
def start_test():
    print("celery test")


# 城区排民统计表
@celery.task(name="generate_excel_city")
def generate_excel_city():
    year = datetime.now().year
    month = datetime.now().month
    file_name = f"{month}月城区排名统计表({year}).xls"
    title = f"{month}月考核汇总统计表(城区组)"
    wb = ExcelUtils(file_name)
    wb._add_sheet("城区片")

    data = list()
    data.append([title] + [""] * 6)
    data.append(
        ["小区名称", "应扣分", "所属社区", "社区平均扣分", "街道内排名", "所属街道", "街道平均扣分", "排名"])
    # 查询出当月第一天的时间戳
    from_stmp = TimesUnit.get_first_day_of_month(year, month)
    row_no = 2
    map_for_sort_community_rank = list()  # 用于社区平均分排名
    map_for_sort_street_rank = list()  # 用于街道平均分排名
    tmp_sort_street_value = list()
    # merge_cells = list()     # 需要合并的单元格
    for streetId, houses in HOUSES.items():
        score_for_street = 0
        realNum = 0
        streetName = STREETS.get(streetId, "1")
        # 将同一个街道的按社区查出来
        mp = dict()
        for (houseName, communityName, type_) in houses:
            if type_ == 2:
                continue
            if not mp.get(communityName):
                mp[communityName] = [houseName]
            else:
                mp[communityName].append(houseName)
            realNum += 1
        if realNum == 0:
            continue
        tmp_sort_community_value = list()
        for coName, houseNames in mp.items():
            score_of_community = 0
            for name in houseNames:
                score_of_house = 0
                plans = Plan.query.filter(
                    Plan.update_at >= from_stmp, Plan.house_name == name,
                    Plan.update_at <= TimesUnit.get_now(),
                    Plan.street_id == streetId).all()
                for plan in plans:
                    score_of_house += sum([
                        abs(i.get('value')) for i in json.loads(plan.content)
                    ])

                row_no += 1
                score_of_community += score_of_house
                data.append(
                    [name, score_of_house, coName, '', '', streetName, '', ''])

            score_of_community = round(score_of_community / len(houseNames), 1)
            _row_from = row_no - len(houseNames)
            _row_to = row_no - 1
            if len(houseNames) != 1:
                wb._merge(_row_from, _row_to, 2, 2, coName)
                wb._merge(_row_from, _row_to, 3, 3, "")
                wb._merge(_row_from, _row_to, 4, 4, "")

            tmp_sort_community_value.append([_row_from, score_of_community])
            score_for_street += score_of_community

        # 对街道进行排序
        sorted_community = sorted([i[1] for i in tmp_sort_community_value])
        for (_row_from, _v) in tmp_sort_community_value:
            index = sorted_community.index(_v) + 1
            map_for_sort_community_rank.append([_row_from, _v, index])

        # 合并街道单元格
        _row_from = row_no - realNum
        _row_to = row_no - 1
        score_of_street = round(score_for_street / realNum, 4)
        wb._merge(_row_from, _row_to, 5, 5, streetName)
        wb._merge(_row_from, _row_to, 6, 6, "")
        wb._merge(_row_from, _row_to, 7, 7, "")
        tmp_sort_street_value.append([_row_from, score_of_street])

    # 街道排名
    sorted_street = sorted([i[1] for i in tmp_sort_street_value])
    for (_row_from, _v) in tmp_sort_street_value:
        index = sorted_street.index(_v) + 1
        map_for_sort_street_rank.append([_row_from, _v, index])

    wb._update(data)
    wb._merge(0, 0, 0, 7, title)
    for [row_1, value_1, index] in map_for_sort_community_rank:
        wb._write(row_1, 3, value_1)
        wb._write(row_1, 4, index)

    for [row_2, value_2, index1] in map_for_sort_street_rank:
        wb._write(row_2, 6, value_2)
        wb._write(row_2, 7, index1)

    wb._save()


# 城镇排民统计表
@celery.task(name="generate_excel_town")
def generate_excel_town():
    year = datetime.now().year
    month = datetime.now().month
    file_name = f"{month}月城镇排名统计表({year}).xls"
    title = f"{month}月考核汇总统计表(城镇组)"
    wb = ExcelUtils(file_name)
    wb._add_sheet("城镇组")

    row_no = 2
    data = list()
    data.append([title] + [""] * 6)
    data.append(
        ["村(小区)名称", "应扣分", "所属街镇", "镇街平均扣分", "排名"])
    # 查询出当月第一天的时间戳
    from_stmp = TimesUnit.get_first_day_of_month(year, month)
    row_no = 2
    map_for_sort_street_rank = list()  # 用于街道平均分排名
    tmp_sort_street_value = list()
    # merge_cells = list()     # 需要合并的单元格
    for streetId, houses in HOUSES.items():
        score_for_street = 0
        streetName = STREETS.get(streetId, "1")
        # 将同一个街道的按社区查出来
        realHouses = list()
        for (houseName, communityName, type_) in houses:
            if type_ == 1:
                continue
            realHouses.append(houseName)
        if len(realHouses) == 0:
            continue

        for name in realHouses:
            score_of_house = 0
            plans = Plan.query.filter(
                Plan.update_at >= from_stmp, Plan.house_name == name,
                Plan.update_at <= TimesUnit.get_now(),
                Plan.street_id == streetId).all()
            for plan in plans:
                score_of_house += sum([abs(i.get('value')) for i in json.loads(plan.content)])

            row_no += 1
            score_for_street += score_of_house
            data.append([name, score_of_house, streetName, '', ''])
            score_for_street += score_of_house

        score_of_street = round(score_for_street / len(realHouses), 1)
        _row_from = row_no - len(realHouses)
        _row_to = row_no - 1
        if len(realHouses) != 1:
            wb._merge(_row_from, _row_to, 2, 2, streetName)
            wb._merge(_row_from, _row_to, 3, 3, score_of_street)
            wb._merge(_row_from, _row_to, 4, 4, "")
        tmp_sort_street_value.append([_row_from, score_of_street])

    # 对街道进行排序
    sorted_street = sorted([i[1] for i in tmp_sort_street_value])
    for (_row_from, _v) in tmp_sort_street_value:
        index = sorted_street.index(_v) + 1
        map_for_sort_street_rank.append([_row_from, _v, index])

    wb._update(data)
    wb._merge(0, 0, 0, 7, title)

    for [row_2, val, index1] in map_for_sort_street_rank:
        wb._write(row_2, 3, val)
        wb._write(row_2, 4, index1)
    wb._save()
