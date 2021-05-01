from server import db
from db.assotiation_tables.tables import user_list


class User(db.Model):
    __tablename__ = "User"
    user_id_seq = db.Sequence("user_id_seq")
    id = db.Column(db.Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value())
    email = db.Column(db.String)
    name = db.Column(db.String)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    lists = db.relationship("List", secondary=user_list, back_populates="users")

    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "sex": self.sex,
            "age": self.age,
            "lists": [list_item.to_dict() for list_item in self.lists]
        }

    def __repr__(self):
        return f"User {self.email}"
