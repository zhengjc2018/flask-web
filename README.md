### flask-web

------


【娱乐项目】

初衷：自动获得每天更新的番或者剧

【使用】
1. export FLASK_ENV=development
2. export FLASK_APP=manage.py
3. flask run --host 0.0.0.0 --no-reload (no-reload参数可以 解决Flask-SocketIO引起的signal only works in main thread问题)