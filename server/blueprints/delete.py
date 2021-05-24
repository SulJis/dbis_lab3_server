from server.blueprints.bp_imports import *

delete = Blueprint("delete", __name__)


@delete.route("/api/delete/note/<note_id>", methods=["DELETE"])
@jwt_required()
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id).first()
    db.session.delete(note)
    db.session.commit()
    return {
        "delete": "success"
    }


@delete.route("/api/delete/list/<list_id>", methods=["DELETE"])
@jwt_required()
def delete_list(list_id):
    curr_list = List.query.filter_by(id=list_id).first()
    db.session.delete(curr_list)
    db.session.commit()
    return {
        "delete": "success"
    }


@delete.route("/api/delete/label/<label_id>", methods=["DELETE"])
@jwt_required()
def delete_label(label_id):
    label = Label.query.filter_by(id=label_id).first()
    db.session.delete(label)
    db.session.commit()
    return {
        "delete": "success"
    }
