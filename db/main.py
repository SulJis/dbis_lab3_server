from db.classes.user import User
from db.classes.note import Note
from db.classes.list import List
from db.classes.label import Label
from server.constants import db, base, session

# session = sessionmaker(db)()
base.metadata.create_all(db)

bodya = User(email="bodya@gmail.com", name="Bohdan", sex="Male", age=20)
note = Note(title="Task", text="Do lab3", checked=False)
list1 = List(title="List1")
list2 = List(title="List2")
label = Label(text="label1", color="black")
list1.notes.append(note)
list1.labels.append(label)
bodya.lists.append(list1)

session.add(bodya)
session.add(note)
session.add(list1)
session.add(list2)
session.add(label)
session.commit()
print(session.query(User).first().to_dict())

