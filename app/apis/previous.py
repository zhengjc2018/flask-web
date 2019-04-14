from flask import Blueprint


bp = Blueprint('test', __name__)


@bp.route('/')
def run():
    return "<a>test apis</a>"
