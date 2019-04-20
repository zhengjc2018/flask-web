import os
from app import create_app, db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, db=db)
    return context


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
