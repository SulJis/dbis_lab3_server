from flask import jsonify

from server.blueprints.bp_imports import *

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email, password, remember = data.values()
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return {"status": "success",
                    "message": "logged in",
                    "data": {
                        "id": user.id,
                        "token": access_token,
                        "email": user.email
                    }
                }
        else:
            return {
                "status": "failed",
                "message": "wrong password"
            }


@auth.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    name, email, password, sex, date = data.values()
    user = User.query.filter_by(email=email).first()
    if not user:
        new_user = User(name=name, email=email, password=generate_password_hash(password), sex=sex, birth_date=date)
        db.session.add(new_user)
        db.session.commit()
    return {"status": "signed up"}


@auth.route("/logout", methods=["POST"])
def logout():
    data = jsonify({
        "logout": "success"
    })
    unset_jwt_cookies(data)
    return data
