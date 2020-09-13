import os


class Markdown2PDF:

    def __init__(self, md_path, pdf_path):
        self.md_path = md_path
        self.pdf_path = pdf_path

    def run(self):
        cmd = f"pandoc '{self.md_file}' -o '{self.pdf_file}' --pdf-engine=xelatex -V mainfont='PingFang SC' --template=template.tex"
        os.system(cmd)
