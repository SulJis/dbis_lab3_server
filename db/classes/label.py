from server import db
from db.assotiation_tables.tables import list_label


class Label(db.Model):
    __tablename__ = "Label"
    text = db.Column(db.String, primary_key=True)
    color = db.Column(db.String)
    lists = db.relationship("List", secondary=list_label, back_populates="labels")

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
