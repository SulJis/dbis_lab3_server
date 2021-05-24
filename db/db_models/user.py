from server import db
from db.assotiation_tables.tables import user_list


class User(db.Model):
    __tablename__ = "User"
    user_id_seq = db.Sequence("user_id_seq")
    id = db.Column(db.Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value())
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    sex = db.Column(db.String)
    birth_date = db.Column(db.DateTime)
    lists = db.relationship("List", secondary=user_list, back_populates="users")
    labels = db.relationship("Label")

    def get_lists(self):
        return sorted([list_item.to_dict() for list_item in self.lists], key=lambda x: x["id"], reverse=True)

    def get_labels(self):
        return sorted([label.to_dict() for label in self.labels], key=lambda x: x["id"])

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "sex": self.sex,
            "birth_date": self.birth_date,
            "lists": self.get_lists(),
            "labels": self.get_labels()
        }

    def __repr__(self):
        return f"User {self.email}"
