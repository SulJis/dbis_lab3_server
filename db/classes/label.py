from server.constants import base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from db.assotiation_tables.tables import list_label


class Label(base):
    __tablename__ = "Label"
    text = Column(String, primary_key=True)
    color = Column(String)
    lists = relationship("List", secondary=list_label, back_populates="labels")

    def to_dict(self):
        return {
            "text": self.text,
            "color": self.color
        }

    def to_dict_with_lists(self):
        data = self.to_dict()
        lists = [list_item.to_dict() for list_item in self.lists]
        data["lists"] = lists
        return data

    def __repr__(self):
        return f"Label {self.text}"
