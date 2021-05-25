# Лабораторна робота №3.
## Сліпченко Максим, КМ-81.
## Опис репозиторію:

### Директорія до запуску програми
```
dbis_lab3
├── wsgi.py - project entrypoint
├── db
│   ├── __init__.py
│   |── main.py -db creation
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
    └── blueprints flask routes blueprints
        |── __init__.py
        |── bp_imports.py
        |── auth.py
        |── create.py
        |── delete.py
        |── read.py
        └── update.py
```

