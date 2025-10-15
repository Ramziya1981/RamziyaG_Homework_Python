import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Строка подключения к БД
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/QA"
# Создание движка и сессии
engine = create_engine(DATABASE_URL)
os.environ['SQLALCHEMY_SILENCE_UBER_WARNING'] = '1'
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Пример модели Student
class Student(Base):
    __tablename__ = 'student'

    user_id = Column(Integer, primary_key=True, index=True)
    level = Column(String, index=True)
    education_form = Column(String, index=True)
    subject_id = Column(Integer, primary_key=True, index=True)
