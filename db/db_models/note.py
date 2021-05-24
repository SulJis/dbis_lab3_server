import datetime

from server import db


class Note(db.Model):
    __tablename__ = "Note"
    note_id_seq = db.Sequence("note_id_seq")
    id = db.Column(db.Integer, note_id_seq, primary_key=True, server_default=note_id_seq.next_value())
    text = db.Column(db.String)
    checked = db.Column(db.Boolean)
    deadline = db.Column(db.Date)
    list_id = db.Column(db.Integer, db.ForeignKey("List.id"))

    def set_deadline(self, deadline):
        if deadline is not None:
            self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "checked": self.checked,
            "list_id": self.list_id,
            "deadline": self.deadline.strftime("%Y-%m-%d") if self.deadline else ""
            }

    def __repr__(self):
        return f"Note {self.title}, text: {self.text}"
