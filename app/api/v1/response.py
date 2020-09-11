from flask import jsonify


def newResponse(data, code, msg=None, pageNo=None, pasgSize=None):
    return jsonify({
        "http_code": code,
        "data": data,
        "msg": msg or ("成功" if code == 200 else "失败"),
        "pageSize": pasgSize,
        "pageNo": pageNo,
    })
