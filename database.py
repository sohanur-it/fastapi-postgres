import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = os.getenv('DATABASE_URL')
# URL_DATABASE = 'postgresql://postgres:postgres@postgres:5432/postgres'
print(URL_DATABASE)

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
