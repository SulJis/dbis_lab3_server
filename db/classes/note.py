from server import db


class Note(db.Model):
    __tablename__ = "Note"
    note_id_seq = db.Sequence("note_id_seq")
    id = db.Column(db.Integer, note_id_seq, primary_key=True, server_default=note_id_seq.next_value())
    title = db.Column(db.String)
    text = db.Column(db.String)
    checked = db.Column(db.Boolean)
    list_id = db.Column(db.Integer, db.ForeignKey("List.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "text": self.text,
            "checked": self.checked,
            "list_id": self.list_id
            }

    def __repr__(self):
        return f"Note {self.title}, text: {self.text}"
