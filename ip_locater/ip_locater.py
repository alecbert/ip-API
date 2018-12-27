from flask import Blueprint

bp = Blueprint('ip_locater', __name__)


@bp.route('/', methods=['GET'])
def index():
    return 'Hello'
