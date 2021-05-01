# from sqlalchemy import Table, Column, String, Integer, ForeignKey
# from server.constants import base
from server import db

user_list = db.Table("User_List", db.metadata,
                     db.Column("user_id", db.Integer, db.ForeignKey("User.id")),
                     db.Column("list_id", db.Integer, db.ForeignKey("List.id")))

list_label = db.Table("List_Label", db.metadata,
                      db.Column("list_id", db.Integer, db.ForeignKey("List.id")),
                      db.Column("label_text", db.String, db.ForeignKey("Label.text")))
