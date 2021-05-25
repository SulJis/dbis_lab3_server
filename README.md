# Лабораторна робота №3.
## Сліпченко Максим, КМ-81.
## Опис репозиторію:
```
dbis_lab3
├── diagrams
├── wsgi.py - project entrypoint
├── db
│   ├── __init__.py
│   |── main.py - db creation script
│   |── assotiation_tables -tables for many ro many relationship
│   │   └── tables.py 
│   └── db_models -sqlalchemy models
│       |── __init__.py
│       |── user.py
│       |── label.py
│       |── note.py
│       └── list.py
└── server
    ├── __init__.py
    └── blueprints - flask routes blueprints
        |── __init__.py
        |── bp_imports.py
        |── auth.py
        |── create.py
        |── delete.py
        |── read.py
        └── update.py
```
# Опис роботи
В якості доменної області для реалізації **CRUD** операцій було обрано менеджер планів та задач. Логічна та фізична діаграми містяться в папці ```diagrams```.

Основні функції веб-додатка:
* Створення нових сутностей: User, List, Label, Note
* Видалення сутностей: List, Label, Note
* Редагування полів сутностей: List, Label, Note
* Фільтрація сутностей List за обраним Label
* Додавання до кожного List нових Label, відкріплення Label з List за потреби

Таким чином (разом з можливістю бачити ці сутності в інтерфейсі) було реалізовано CRUD сценарій користування додатком.

# Інструкція для розгортання

Для створення бази даних (робиться тільки один раз) необхідно виконати команду
```
python db/main.py
```
Для запуску сервера необхідно виконати команду
```
python server/__init__.py #for developing
gunicorn wsgi:app
```
Посилання на репозиторій клієнта (з інструкцією розгортання там же):https://github.com/SulJis/dbis_lab3_client
# Посилання на розгорнутий додаток на Heroku
https://suljis-vue-todo-client.herokuapp.com
