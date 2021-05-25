# Лабораторна робота №3.
## Сліпченко Максим, КМ-81.
## Опис репозиторію:
```
dbis_lab3
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

В якості доменної області для реалізації **CRUD** операцій було обрано менеджер планів та задач.
![alt text](http://www.plantuml.com/plantuml/png/XP2nJiGm38PtFqLcH5_WffjOG8ZbvifjB2N2JL3YmY7eknDB5wBII2nj_F-_FySvPy4awy90GRnycakcz0LttfxCowCfXKU6OG1QqFF9l6EQ7IO8k52htZ3dZvZiw32x9ay-YHijIedg5p9Tcxj1dVdai_Hc5fEfsu0JyQ5ZBVzHfOSTXAxI67Fac7h8voXq8BBFyY_HqVnA9JF5o609BVjG5zxlEDPxLsuPTT_OHLU_OpJCHNUylPVkswKKkm_vxJRRzp0OFVtLj0Hejst9ewX707qviyMQkWLYPPqfs7NX7m00)
