from server import db
from db.assotiation_tables.tables import list_label


class Label(db.Model):
    __tablename__ = "Label"
    label_id_seq = db.Sequence("label_id_seq")
    id = db.Column(db.Integer, label_id_seq, primary_key=True, server_default=label_id_seq.next_value())
    text = db.Column(db.String)
    color = db.Column(db.String)
    lists = db.relationship("List", secondary=list_label, back_populates="labels")
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "color": self.color
        }

    def get_lists(self):
        return sorted([list_item.to_dict() for list_item in self.lists], key=lambda x: x["id"])

    def __repr__(self):
        return f"Label {self.text}"
