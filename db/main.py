import datetime

from db.db_models import *
from server import db, create_app
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()
with app.app_context():
    db.drop_all()
    db.create_all()
    user = User(email="test@gmail.com", password=generate_password_hash("test"), name="Test", sex="Male", birth_date=datetime.datetime.now())
    note = Note(text="Do lab3", checked=True)
    list1 = List(title="DBIS")
    list2 = List(title="List2")
    label = Label(text="label1", color="dark")
    label2 = Label(text="Label second", color="blue")
    user.labels.append(label2)
    list1.notes.append(note)
    user.labels.append(label)
    list1.labels.append(label)
    user.lists.append(list1)
    note2 = Note(text="Do another staff", checked=False, deadline=datetime.datetime.now())
    list2.notes.append(note2)
    list2.labels.append(label2)
    user.lists.append(list2)
    db.session.add(user)
    db.session.add(note)
    db.session.add(list1)
    db.session.add(list2)
    db.session.add(label)
    db.session.commit()
    print(db.session.query(User).first().to_dict())
