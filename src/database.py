from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#url_database = 'mysql+pymysql://root:mart@localhost:3306/books' #replace with your mysql database for conection to mysql

url_database = "sqlite:///database.db"

engine = create_engine(url_database)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()





