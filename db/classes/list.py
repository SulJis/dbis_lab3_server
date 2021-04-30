from server.constants import base
from sqlalchemy import Column, String, Integer, Sequence, Boolean
from sqlalchemy.orm import relationship
from db.assotiation_tables.tables import user_list, list_label


class List(base):
    __tablename__ = "List"
    list_id_seq = Sequence("list_id_seq")
    id = Column(Integer, list_id_seq, primary_key=True, server_default=list_id_seq.next_value())
    title = Column(String)
    users = relationship("User", secondary=user_list, back_populates="lists")
    labels = relationship("Label", secondary=list_label, back_populates="lists")
    notes = relationship("Note")

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
