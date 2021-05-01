from server import db
from db.assotiation_tables.tables import list_label, user_list


class List(db.Model):
    __tablename__ = "List"
    list_id_seq = db.Sequence("list_id_seq")
    id = db.Column(db.Integer, list_id_seq, primary_key=True, server_default=list_id_seq.next_value())
    title = db.Column(db.String)
    users = db.relationship("User", secondary=user_list, back_populates="lists")
    labels = db.relationship("Label", secondary=list_label, back_populates="lists")
    notes = db.relationship("Note")

    def to_dict(self):
        data = {
            "id": self.id,
            "title": self.title,
            # "users": [],
            "labels": [],
            "notes": []
        }
        # for user in self.users:
        #     data["users"].append(user.to_dict())
        for label in self.labels:
            data["labels"].append(label.to_dict())
        for note in self.notes:
            data["notes"].append(note.to_dict())
        return data

    def __repr__(self):
        return f"List {self.title}"
