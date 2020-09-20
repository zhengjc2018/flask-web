# coding=UTF-8
import xlrd
import xlwt
from datetime import datetime
from shutil import copyfile
from xlrd import open_workbook
from xlutils.copy import copy


class ExcelUtils:

    def __init__(self, new_file_name):
        self._wb = xlwt.Workbook()
        self._filename = new_file_name
        # 设置样式
        self._style = xlwt.XFStyle()
        al = xlwt.Alignment()
        al.horz = 0x02      # 设置水平居中
        al.vert = 0x01      # 设置垂直居中
        self._style.alignment = al

    def _add_sheet(self, sheet_name="测试"):
        self._sheet = self._wb.add_sheet(sheet_name, cell_overwrite_ok=True)

    def _update(self, data=[[]]):
        for i in range(len(data[0])):
            col = self._sheet.col(i)
            col.width = 256*20
        for i, j in enumerate(data):
            for k, v in enumerate(j):
                self._write(i, k, v)

    def _write(self, row, col, data):
        self._sheet.write(row, col, str(data), self._style)

    def _merge(self, row1, row2, col1, col2, content):
        self._sheet.write_merge(row1, row2, col1, col2, str(content), self._style)

    def _save(self):
        self._wb.save(self._filename)


def test():
    year = datetime.now().year
    month = datetime.now().month
    file_name = f"{month}月城区排名统计表({year}).xls"
    title = f"{month}月考核汇总统计表(城区组)"
    wb = ExcelUtils(file_name)
    wb._add_sheet("城区片")

    data = list()
    data.append([title]+[""]*6)
    data.append(["小区名称", "应扣分", "所属社区", "社区平均扣分", "街道内排名",
                "所属街道", "街道平均扣分", "排名"])
    wb._update(data)
    wb._merge(0, 0, 0, 7, title)
    wb._save()


if __name__ == "__main__":
    # test()
    a = (("a", 1, 2), ("b", 222, 2222))
    print(sorted(a, key=lambda x: x[1], reverse=True))
