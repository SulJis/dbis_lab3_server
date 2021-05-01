from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:vfrcbv2001@localhost:5432/postgres"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    from server.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from server.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
