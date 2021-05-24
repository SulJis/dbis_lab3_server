import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()


def create_app():
    url = os.environ.get("DATABASE_URL").split("//")[1]
    sqlalchemy_uri = f"postgresql+psycopg2://{url}"
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "SECRET_KEY"
    app.config["SQLALCHEMY_DATABASE_URI"] = sqlalchemy_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config["JWT_SECRET_KEY"] = "SECRET_KEY"
    CORS(app)

    db.init_app(app)
    jwt = JWTManager(app)

    from server.blueprints import auth_blueprint, create_blueprint, read_blueprint, update_blueprint, delete_blueprint
    blueprints = [auth_blueprint, create_blueprint, read_blueprint, update_blueprint, delete_blueprint]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
