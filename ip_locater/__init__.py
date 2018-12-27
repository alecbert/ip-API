from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from . import createDB

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # createDB.init_db()
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///ip_addresses.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False)
    db.init_app(app)

    from . import ip_locater
    app.register_blueprint(ip_locater.bp)

    return app
