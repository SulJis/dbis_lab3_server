from server.constants import base
from sqlalchemy import Column, String, Integer, Sequence, Boolean, ForeignKey


class Note(base):
    __tablename__ = "Note"
    note_id_seq = Sequence("note_id_seq")
    id = Column(Integer, note_id_seq, primary_key=True, server_default=note_id_seq.next_value())
    title = Column(String)
    text = Column(String)
    checked = Column(Boolean)
    list_id = Column(Integer, ForeignKey("List.id"))

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
