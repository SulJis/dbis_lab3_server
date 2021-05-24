from server.blueprints.bp_imports import *

update = Blueprint("update", __name__)


@update.route("/api/update/list/<list_id>/add-label/<label_id>", methods=["PUT"])
@jwt_required()
def add_label(label_id, list_id):
    label = Label.query.filter_by(id=label_id).first()
    list_obj = List.query.filter_by(id=list_id).first()
    if label not in list_obj.labels:
        list_obj.labels.append(label)
        db.session.commit()
        return {
            "addition": "success",
            "label": label.to_dict()
        }
    else:
        return {
            "addition": "fault",
            "message": "this label is already in list"
        }, 500


@update.route("/api/update/list/<list_id>/unpin/<label_id>", methods=["PUT"])
@jwt_required()
def unpin_label(label_id, list_id):
    label = Label.query.filter_by(id=label_id).first()
    list_obj = List.query.filter_by(id=list_id).first()
    list_obj.labels.remove(label)
    db.session.commit()
    return {
        "unpin": "success",
    }


@update.route("/api/update/note/<note_id>", methods=["PUT"])
@jwt_required()
def update_note(note_id):
    data = request.get_json()
    note = Note.query.filter_by(id=note_id).update(data)
    db.session.commit()
    return {
        "update": "success"
    }


@update.route("/api/update/list/<list_id>", methods=["PUT"])
@jwt_required()
def update_list(list_id):
    data = request.get_json()
    list_obj = List.query.filter_by(id=list_id).first()
    list_obj.title = data["title"]
    db.session.commit()
    return {
        "update": "success"
    }


@update.route("/api/update/label/<label_id>", methods=["PUT"])
@jwt_required()
def update_label(label_id):
    data = request.get_json()
    label = Label.query.filter_by(id=label_id).first()
    label.text = data["text"]
    label.color = data["color"]
    db.session.commit()
    return {
        "update": "success",
    }
