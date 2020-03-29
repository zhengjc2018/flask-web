import os
from app import create_app, db
from app.models.slave import Slave


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, db=db)
    return context


@app.cli.command("init_db")
def init_db():
    item = [(1, "动漫"), (2, "日剧"), (3, "电影"), (4, "综艺"), (5, "小说")]
    for i in item:
        obj = Slave.query.get(i[0])
        if not obj:
            obj = Slave(id=i[0])
        obj.name = i[1]
        db.session.add(obj)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=8080)
