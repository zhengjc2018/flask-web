import os
import zipfile


# 打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            zipf.write(pathfile, filename)
    zipf.close()


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "app", "static", "report")
    make_zip(path, "dsd.zip")
