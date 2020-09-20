# coding=UTF-8
import xlrd
import xlwt
from shutil import copyfile
from xlrd import open_workbook
from xlutils.copy import copy


class ExcelUtils:

    def __init__(self, new_file_name):
        self._wb = xlwt.Workbook()
        self._filename = new_file_name

    def _update(self, sheet_name="测试", data=[[]]):
        self._sheet = self._wb.add_sheet(sheet_name, cell_overwrite_ok=True)
        for i, j in enumerate(data):
            for k, v in enumerate(j):
                self._sheet.write(i, k, str(v))

    def _merge(self, row1, row2, col1, col2, content):
        self._sheet.write_merge(row1, row2, col1, col2, content)

    def _save(self):
        self._wb.save(self._filename)


def test(new_file_name):
    a = ExcelUtils(new_file_name)
    a._update(data=[["test", "name"], [1, 2], [2, 4]])
    a._merge(0, 1, 0, 0, "hh")
    a._save()


if __name__ == "__main__":
    test("test2.xls")
