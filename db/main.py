from db.classes.user import User
from db.classes.note import Note
from db.classes.list import List
from db.classes.label import Label
from server import db, create_app

app = create_app()
app.app_context().push()
with app.app_context():
    db.drop_all()
    db.create_all()
    bodya = User(email="bodya@gmail.com", name="Bohdan", sex="Male", age=20)
    note = Note(title="Task", text="Do lab3", checked=False)
    list1 = List(title="List1")
    list2 = List(title="List2")
    label = Label(text="label1", color="black")
    list1.notes.append(note)
    list1.labels.append(label)
    bodya.lists.append(list1)

    db.session.add(bodya)
    db.session.add(note)
    db.session.add(list1)
    db.session.add(list2)
    db.session.add(label)
    db.session.commit()
    print(db.session.query(User).first().to_dict())
