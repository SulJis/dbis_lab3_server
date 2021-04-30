from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


base = declarative_base()
db = create_engine("postgresql+psycopg2://postgres:vfrcbv2001@localhost:5432/postgres")
session = sessionmaker(db)()
