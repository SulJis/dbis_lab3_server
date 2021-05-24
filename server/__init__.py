import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()


def create_app():
    url = os.environ.get("DB_URL")
    port = os.environ.get("DB_PORT")
    user = os.environ.get("DB_USER")
    pwd = os.environ.get("DB_PASSWORD")
    dbms = os.environ.get("DB_MS")
    name = os.environ.get("DB_NAME")
    flask_secret_key = os.environ.get("FLASK_SECRET_KEY")
    jwt_secret_key = os.environ.get("JWT_SECRET_KEY")

    sqlalchemy_uri = f"{dbms}://{user}:{pwd}@{url}:{port}/{name}"
    app = Flask(__name__)
    app.config["SECRET_KEY"] = flask_secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = sqlalchemy_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["JWT_SECRET_KEY"] = jwt_secret_key
    CORS(app)

    db.init_app(app)
    jwt = JWTManager(app)

    from server.blueprints import auth_blueprint, create_blueprint, read_blueprint, update_blueprint, delete_blueprint
    blueprints = [auth_blueprint, create_blueprint, read_blueprint, update_blueprint, delete_blueprint]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
