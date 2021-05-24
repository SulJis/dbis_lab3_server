from server.blueprints.bp_imports import *

create = Blueprint("create", __name__)


@create.route("/api/create/note", methods=["POST"])
@jwt_required()
def create_note():
    data = request.get_json()

    note_text = data["text"]
    note_deadline = data["deadline"]
    list_id = data["listId"]
    if note_text is None:
        return {
            "status": "fault",
            "message": "invalid text for note"
        }, 500
    new_note = Note(text=note_text, checked=False)
    new_note.set_deadline(note_deadline)
    list_for_note = List.query.filter_by(id=list_id).first()
    list_for_note.notes.append(new_note)
    db.session.commit()

    return new_note.to_dict()


@create.route("/api/create/list", methods=["POST"])
@jwt_required()
def create_list():
    data = request.get_json()
    title = data["title"]
    if title is None:
        return {
               "status": "fault",
               "message": "invalid title for list"
           }, 500
    user = User.query.filter_by(id=get_jwt_identity()).first()
    new_list = List(title=title)
    user.lists.append(new_list)
    db.session.commit()

    return new_list.to_dict()


@create.route("/api/create/label", methods=["POST"])
@jwt_required()
def create_label():
    data = request.get_json()
    if data["text"] is None:
        return {
               "status": "fault",
               "message": "invalid text for label"
           }, 500
    label = Label(text=data["text"], color=data["color"])
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    user.labels.append(label)
    db.session.commit()
    return label.to_dict()
