from server import db
from db.assotiation_tables.tables import list_label, user_list
import json


class List(db.Model):
    __tablename__ = "List"
    list_id_seq = db.Sequence("list_id_seq")
    id = db.Column(db.Integer, list_id_seq, primary_key=True, server_default=list_id_seq.next_value())
    title = db.Column(db.String)
    users = db.relationship("User", secondary=user_list, back_populates="lists")
    labels = db.relationship("Label", secondary=list_label, back_populates="lists", cascade="save-update")
    notes = db.relationship("Note")

    def to_dict(self):
        data = {
            "id": self.id,
            "title": self.title
        }
        return data

    def aggregations_to_dict(self):
        data = {
            "id": self.id,
            "title": self.title,
            "labels": self.get_labels(),
            "notes": self.get_notes()
        }
        return data

    def get_notes(self):
        return sorted([note.to_dict() for note in self.notes], key=lambda x: x["id"])

    def get_labels(self):
        return sorted([label.to_dict() for label in self.labels], key=lambda x: x["id"])

    def __repr__(self):
        return f"List {self.title}"
