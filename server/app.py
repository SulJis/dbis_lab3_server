from flask import Flask
import json
from server.constants import db, base
from sqlalchemy.orm import sessionmaker
from db.classes.user import User
from db.classes.note import Note
from db.classes.list import List
from db.classes.label import Label


app = Flask(__name__)
session = sessionmaker(db)()


@app.route('/')
def home():
    return "hello"


@app.route("/api/get/<user_id>/")
def get_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user.to_dict()


if __name__ == '__main__':
    app.run()
