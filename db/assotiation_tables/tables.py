from sqlalchemy import Table, Column, String, Integer, ForeignKey
from server.constants import base

user_list = Table("User_List", base.metadata,
                  Column("user_id", Integer, ForeignKey("User.id")),
                  Column("list_id", Integer, ForeignKey("List.id")))

list_label = Table("List_Label", base.metadata,
                   Column("list_id", Integer, ForeignKey("List.id")),
                   Column("label_text", String, ForeignKey("Label.text")))
