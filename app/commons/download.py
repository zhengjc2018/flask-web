import os
from flask import make_response, send_file, request, current_app
from urllib import parse


def download_file(file_name):
    # 解决中文下载问题
    file_name = parse.unquote(request.args.get("fileName"))
    base_dir = current_app.config['RAW_REPORT_FOLDER']

    file_name = os.path.join(base_dir, file_name)
    response = make_response(send_file(file_name))
    basename = os.path.basename(file_name)
    response.headers["Content-Disposition"] = \
        "attachment;" \
        "filename*=UTF-8''{utf_filename}".format(
            utf_filename=parse.quote(basename.encode('utf-8'))
    )
    return response
