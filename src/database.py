from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#rl_database = 'mysql+pymysql://root:mart@localhost:3306/books'

url_database = "sqlite:///database.db"

engine = create_engine(url_database)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()





