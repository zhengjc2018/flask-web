import os
from app import create_app, db
from app.models import Users
from app.commons import TimesUnit
from werkzeug.security import generate_password_hash


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, db=db)
    return context


@app.cli.command("init_db")
def init_db():
    user = Users(
        login_name="super",
        login_pass=generate_password_hash("super"),
        desc="superUser",
        update_at=TimesUnit.get_now()
    )
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=8080)
