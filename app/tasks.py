from flask import current_app
import json
import os
from app.extensions import celery
from datetime import datetime
import datetime as dt
from app.commons import ExcelUtils, WordUtils, TimesUnit
from app.models import Plan, PenaltiesRule, History
from app.static import STREETS, HOUSES


@celery.task(name='start_test')
def start_test():
    print("celery test")


# 获取当前一个月内 城区的排名,
def get_rank_for_city(is_city=True):
    title, file_name, from_stmp = get_excel_info(True)
    tmpResults = list()
    finalResult = list()
    totalNum = 0
    for streetId, houses in HOUSES.items():
        streetName = STREETS.get(streetId, "1")
        # 将同一个街道的按社区查出来
        realHouses = list()
        tag = 2 if is_city else 1

        for (houseName, communityName, type_) in houses:
            if type_ == tag:
                continue
            realHouses.append((houseName, communityName))

        for (name, coName) in realHouses:
            score_of_house = 0
            plans = Plan.query.filter(Plan.update_at >= from_stmp,
                                      Plan.update_at <= TimesUnit.get_now(),
                                      Plan.house_name == name,
                                      Plan.street_id == streetId).all()
            # 获取某个小区所有的扣分项
            for plan in plans:
                score_of_house += sum([abs(i.get('value')) for i in json.loads(plan.content)])
            tmpResults.append([name, score_of_house, coName, streetName])
        totalNum += len(realHouses)


    # 进行排名
    scores = sorted([float(i[1]) for i in tmpResults])
    for (name, score_of_house, coName, streetName) in tmpResults:
        rank = scores.index(score_of_house)
        finalResult.append([name, score_of_house, rank, coName, streetName])

    return finalResult, totalNum


def get_excel_info(is_city=False):
    basePath = current_app.config['RAW_REPORT_FOLDER']
    year = datetime.now().year
    month = datetime.now().month
    area = "城区" if is_city else "城镇"
    file_name = os.path.join(basePath, f"{month}月{area}排名统计表({year}).xls")
    title = f"{month}月考核汇总统计表({area}组)"
    from_stmp = TimesUnit.get_first_day_of_month(year, month)
    return title, file_name, from_stmp


# 生成单个的垃圾分类督查科考核反馈表
def get_check_table(wd, street_id, from_stmp, picture_postion=0, Map=dict(), is_city=True, all_ok=False, time_range=86400):
    streetName = STREETS.get(street_id, "1")
    wd._add_heading("垃圾分类督查科考核反馈表", level=1, size=15)
    data = [["小区(村)\n时间", "项目", "问题点"]]
    merge_rows = list()
    merge_tag = 1
    t = 1 if is_city else 2
    add_title = False
    for (houseName, _, type_) in HOUSES.get(street_id):
        if not (is_city and type_ == t) and not all_ok:
            continue
        plan = Plan.query.filter(Plan.update_at <= from_stmp+time_range,
                                 Plan.update_at >= from_stmp,
                                 Plan.house_name == houseName,
                                 Plan.street_id == street_id).first()

        if not plan:
            continue

        _date = TimesUnit.timestp_to_date(plan.update_at)
        if not add_title:
            wd._add_paragraph(
                    f"时间：{_date.tm_mon}月{_date.tm_mday}日                                                              街道(镇)：{streetName}"
            )
            add_title = True

        is_first = False
        tmp_num = 0
        ruleString = ""
        for jsonData in json.loads(plan.content):
            itemName = jsonData.get("itemName")
            rules = jsonData.get("rule")
            value = jsonData.get("value")
            if int(value) == 0:
                continue
            fileName = jsonData.get("fileName")
            tmp_num += 1

            for i, j in enumerate(rules):
                _tmp = []
                for pic in fileName[i]:
                    picture_postion += 1
                    Map[picture_postion] = pic
                    _tmp.append(str(picture_postion))
                picStr = ", ".join(_tmp)
                ruleString += f"{i+1}. {j} (图 {picStr})\n"

            hs = f"{houseName}({_date.tm_hour}:{_date.tm_min})" if not is_first else ""
            is_first = True
            data.append([hs, itemName, ruleString])

        if tmp_num > 1:
            merge_rows.append((merge_tag, merge_tag + tmp_num - 1))
        merge_tag += tmp_num + 1

    table = wd._add_table(len(data), 3, data)
    # 合并单元格
    for (row1, row2) in merge_rows:
        wd._merge(table, row1 - 1, 0, row2 - 1, 0)
    wd._add_page_break()
    return wd, picture_postion, Map


# 城区排民统计表
@celery.task(name="generate_excel_city")
def generate_excel_city():
    title, file_name, from_stmp = get_excel_info(False)
    wb = ExcelUtils(file_name)
    wb._add_sheet("城区片")

    data = list()
    data.append([title] + [""] * 6)
    data.append(
        ["小区名称", "应扣分", "所属社区", "社区平均扣分", "街道内排名", "所属街道", "街道平均扣分", "排名"])
    # 查询出当月第一天的时间戳
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
    History.insert_(file_name, 1, "")


# 城镇排民统计表
@celery.task(name="generate_excel_town")
def generate_excel_town():
    title, file_name, from_stmp = get_excel_info(True)
    wb = ExcelUtils(file_name)
    wb._add_sheet("城镇组")

    data = list()
    data.append([title] + [""] * 6)
    data.append(["村(小区)名称", "应扣分", "所属街镇", "镇街平均扣分", "排名"])
    # 查询出当月第一天的时间戳
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

        step = 0
        for name in realHouses:
            score_of_house = 0
            plans = Plan.query.filter(Plan.update_at >= from_stmp,
                                      Plan.house_name == name,
                                      Plan.update_at <= TimesUnit.get_now(),
                                      Plan.street_id == streetId).all()
            # 没有数据没有检查
            if not plans:
                continue

            for plan in plans:
                score_of_house += sum(
                    [abs(i.get('value')) for i in json.loads(plan.content)])

            row_no += 1
            step += 1
            score_for_street += score_of_house
            data.append([name, score_of_house, streetName, '', ''])
            score_for_street += score_of_house

        score_of_street = round(score_for_street / step, 1) if step else 0
        _row_from = row_no - step
        _row_to = row_no - 1
        if step > 1:
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
    History.insert_(file_name, 1, "")


# 生成 垃圾分类督查科考核反馈表
@celery.task(name="generate_assessment_form")
def generate_assessment_form():
    basePath = current_app.config['RAW_REPORT_FOLDER']
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    now = TimesUnit.get_now()

    if dt.date(year, month, day).week() == 0:
        range_ = 403200
    else:
        range_ = 172800

    for street_id, houses in HOUSES.items():
        Map = dict()
        picture_postion = 0
        streetName = STREETS.get(street_id, "1")
        fileName = f"垃圾分类督查科考核反馈表_{streetName}_{year}年{month}月{day}日.docx"
        wd = WordUtils(os.path.join(basePath, fileName))
        wd, picture_postion, Map = get_check_table(wd, street_id, now-range_, picture_postion, Map=dict(),
                                                   all_ok=True, time_range=range_)

        for i, picture in Map.items():
            wd._add_picture(picture)
            wd._add_paragraph(f" 图 {i}")
        wd._save()
        History.insert_(os.path.join(basePath, fileName), 1, "")

        # wd._add_heading("垃圾分类督查科考核反馈表", level=1, size=15)
        # wd._add_paragraph(
        #     f"时间：{month}月{day}日                                                              街道(镇)：{streetName}"
        # )

        # data = [title]
        # for (houseName, _, _) in houses:
        #     plan = Plan.query.filter(Plan.update_at <= now,
        #                              Plan.update_at >= now - 86400,
        #                              Plan.house_name == houseName,
        #                              Plan.street_id == streetId).first()

        #     result = {}
        #     if not plan:
        #         continue
        #     # else:
        #     for jsonData in json.loads(plan.content):
        #         itemName = jsonData.get("itemName")
        #         rules = jsonData.get("rule")
        #         if result.get(itemName):
        #             result[itemName] += rules
        #         else:
        #             result[itemName] = rules

        #     is_first = False
        #     for k, v in result.items():
        #         hs = f"{houseName}({datetime.fromtimestamp(plan.update_at)})" if not is_first else ""
        #         is_first = True
        #         tmp = [
        #             hs, k,
        #             "".join([f"{i+1}.{j};\n" for i, j in enumerate(set(v))])
        #         ]
        #         data.append(tmp)
        #     if len(result) > 1:
        #         merge_rows.append((tag, tag + len(result) - 1))
        #     tag += len(result) + 1

        # table = wd._add_table(len(data), 3, data)
        # for (row1, row2) in merge_rows:
        #     wd._merge(table, row1 - 1, 0, row2 - 1, 0)
        # wd._save()


@celery.task(name="generate_assessment_total")
def generate_assessment_total():
    basePath = current_app.config['RAW_REPORT_FOLDER']
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    fileName = f"{month}月份垃圾分类考核情况汇总({year}).docx"

    cityData, cityNum = get_rank_for_city(True)
    townData, townNum = get_rank_for_city(False)
    cityMarks = round(sum([float(i[1]) for i in cityData])/len(cityData), 3)
    townMarks = round(sum([float(i[1]) for i in townData])/len(townData), 3)

    topBestCity = sorted(cityData, key=lambda x: x[1])[:10]
    topWrongCity = sorted(cityData, key=lambda x: x[1])[-10:-1]
    topBestTown = sorted(townData, key=lambda x: x[1])[:10]
    topWrongTown = sorted(townData, key=lambda x: x[1])[-10:-1]

    wd = WordUtils(os.path.join(basePath, fileName))
    wd._add_heading(f"{month}月份垃圾分类考核情况汇总", level=1, size=8)
    wd._add_paragraph(
        f"    {month}月份城区组共检查小区（村）{len(cityData)}个，实现街道、社区的全覆盖，小区检查覆盖率约{round(len(cityData)/cityNum, 4)}%；城镇组共检查村（小区）{len(townData)}个，实现镇、街道的全覆盖，村（小区）检查覆盖率约为{round(len(townData)/townNum, 3)}%。"
    )

    wd._add_paragraph(f"现就{month}月有关检查考核结果作初步梳理汇总：", size=8)

    wd._add_paragraph(f"一、下表为城区片和城镇片{month}月平均扣分情况：", size=8)
    wd._add_table(3, 2, [["", f"{month}月"], ["城区", f"{cityMarks}"], ["城镇", f"{townMarks}"]])

    wd._add_paragraph(f"二、{month}月份城区片和城镇片失分最多和最少村、小区TOP10：", size=8)
    wd._add_paragraph("（一）城区片失分最少小区：", size=8)
    title = ["小区名称", "应扣分", "名次", "所属社区", "所属街道"]
    townTitle = ["小区名称", "应扣分", "名次", "所属街道"]
    wd._add_table(11, 5, [title]+topBestCity)

    wd._add_paragraph("（二）城区片失分最多小区：", size=8)
    wd._add_table(11, 5, [title]+topWrongCity)

    wd._add_paragraph("（三）城镇片失分最少村（小区）：", size=8)
    wd._add_table(11, 4, [townTitle]+topBestTown)

    wd._add_paragraph("（四）城镇片失分最多村（小区）：", size=8)
    wd._add_table(11, 4, [townTitle]+topWrongTown)

    wd._add_paragraph(f"三、下图为城区片和城镇片各镇街{month}月排名情况：", size=8)

    cityPicName = os.path.join(basePath, f"{year}_{month}_城区.png")
    townPicName = os.path.join(basePath, f"{year}_{month}_城镇.png")
    wd.get_picture(cityPicName, [i[0] for i in topBestCity], [i[1] for i in topBestCity], "失分最少的城区")
    wd.get_picture(townPicName, [i[0] for i in topBestTown], [i[1] for i in topBestTown], "失分最少的城镇")
    wd._add_picture(cityPicName)
    wd._add_picture(townPicName)

    wd._add_paragraph("绍兴市求实文化事务中心", right=True)
    wd._add_paragraph(f"{year}.{month},{day}", right=True)
    wd._save()

    History.insert_(os.path.join(basePath, fileName), 1, "")

# 城区报表生成
@celery.task(name="generate_assessment_form_for_month")
def generate_assessment_form_for_month():
    basePath = current_app.config['RAW_REPORT_FOLDER']
    year = datetime.now().year
    month = datetime.now().month
    from_stmp = TimesUnit.get_first_day_of_month(year, month)

    for is_city in [True, False]:
        name = "城区" if is_city else "城镇"
        fileName = f"{year}年{month}月检查台账({name}).docx"
        wd = WordUtils(os.path.join(basePath, fileName))
        # to_stmps = TimesUnit.get_all_wanted_week_timestp(from_stmp, TimesUnit.get_now())
        picture_postion = 0
        Map = dict()

        for street_id, _ in HOUSES.items():
            wd, picture_postion, Map = get_check_table(wd, street_id, from_stmp, picture_postion, Map, is_city, time_range=TimesUnit.get_now()-from_stmp)

        for i, picture in Map.items():
            wd._add_picture(picture)
            wd._add_paragraph(f"图 {i}")

        wd._save()
        History.insert_(os.path.join(basePath, fileName), 2, "")
