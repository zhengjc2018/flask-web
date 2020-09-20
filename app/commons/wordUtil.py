import os
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.shared import Pt
from docx.oxml.ns import qn


class WordUtils:

    def __init__(self, fileName):
        self._file = fileName
        self._doc = Document()

        # 设置默认字体
        self._doc.styles['Normal'].font.name = '微软雅黑'
        self._doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    # 添加段落
    def _add_paragraph(self, content, style="ListBullet", bold=False):
        paragraph = self._doc.add_paragraph()
        run = paragraph.add_run(content)
        run.bold = bold
        return paragraph

    # 添加标题
    def _add_heading(self, content, level=2):
        self._doc.add_heading(content, level)

    # 添加分页符
    def _add_page_break(self):
        self._doc.add_page_break()

    # 添加表格
    def _add_table(self, rows, cols, data=[[]], style="Table Grid"):
        table = self._doc.add_table(rows, cols)
        table.style = style
        for i in range(rows):
            for j in range(cols):
                table.cell(i, j).text = data[i][j]

    # 添加图片
    def _add_picture(self, location, width=1):
        self._doc.add_picture(location, width=Inches(width))

    # 添加章节
    def _add_section(self):
        return self._doc.add_section(WD_SECTION.ODD_PAGE)

    # 保存文件
    def _save(self):
        self._doc.save(self._file)


def test():
    a = WordUtils("test.docx")
    a._add_heading('Test Heading')
    section = a._add_section()
    section.orientation = WD_ORIENT.LANDSCAPE
    # section.page_width = 10
    # section.page_height = 75
    a._add_paragraph("test paragraph")
    a._add_page_break()
    a._add_table(3, 2, [["name", "age"], ["dasd", "12"], ["das2", "43"]])
    a._save()


if __name__ == "__main__":
    test()
