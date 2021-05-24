from server.blueprints.bp_imports import *

read = Blueprint("read", __name__)


@read.route("/api/get_user", methods=["GET"])
@jwt_required()
def get_user():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    return user.to_dict()


@read.route("/api/get/lists", methods=["GET"])
@jwt_required()
def get_lists():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    return {
        "lists": user.get_lists()
    }


@read.route("/api/get/labels", methods=["GET"])
@jwt_required()
def get_labels():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    return {
        "labels": user.get_labels()
    }


@read.route("/api/get/label/<label_id>", methods=["GET"])
@jwt_required()
def get_label(label_id):
    label = Label.query.filter_by(id=label_id).first()
    return label.to_dict()


@read.route("/api/get/list/<list_id>", methods=["GET"])
@jwt_required()
def get_list(list_id):
    list_obj = List.query.filter_by(id=list_id).first()
    return list_obj.aggregations_to_dict()


@read.route("/api/get/lists/by-label/<label_id>", methods=["GET"])
@jwt_required()
def get_lists_by_label(label_id):
    label = Label.query.filter_by(id=label_id).first()
    return {
        "lists": label.get_lists()
    }


@read.route("/api/get/note/<note_id>", methods=["GET"])
@jwt_required()
def get_note(note_id):
    note_obj = Note.query.filter_by(id=note_id).first()
    return note_obj.to_dict()
