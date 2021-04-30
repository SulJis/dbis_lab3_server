from server.constants import base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from db.assotiation_tables.tables import user_list


class User(base):
    __tablename__ = "User"
    user_id_seq = Sequence("user_id_seq")
    id = Column(Integer, user_id_seq, primary_key=True, server_default=user_id_seq.next_value())
    email = Column(String)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    lists = relationship("List", secondary=user_list, back_populates="users")

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
