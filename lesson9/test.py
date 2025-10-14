import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Строка подключения к БД
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/QA"

# Создание движка и сессии
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Пример модели Student
class Student(Base):
    __tablename__ = 'student'

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


# Фикстура для очистки данных после теста
@pytest.fixture(autouse=True)
def clear_data():
    yield
    session.query(Student).delete()
    session.commit()


# Тест на добавление студента
def test_add_student():
    studentName = "Иван Петров"
    print('Создаем сущность Студент с именем: ' + studentName)
    new_student = Student(user_id=1, name=studentName, age=20)
    session.add(new_student)
    session.commit()

    # Проверка добавления
    student = session.query(Student).filter_by(name=studentName).first()
    assert student is not None
    assert student.age == 20

    # Удаляем за собой созданное
    student = session.query(Student).filter_by(name=studentName).first()
    session.delete(student)
    print('Удаляем сущность Студент с именем: ' + studentName)


# Тест на обновление студента
def test_update_student():
    # Сначала создаем запись
    studentName = "Анна Сидорова"
    print('Создаем сущность Студент с именем: ' + studentName)
    new_student = Student(name=studentName, age=21)
    session.add(new_student)
    session.commit()

    # Обновляем данные
    student = session.query(Student).filter_by(name=studentName).first()
    student.age = 22
    session.commit()

    # Проверяем обновление
    updated_student = session.query(Student).filter_by(
        name=studentName
        ).first()
    assert updated_student.age == 22

    # Удаляем за собой созданное
    student = session.query(Student).filter_by(name=studentName).first()
    session.delete(student)
    print('Удаляем сущность Студент с именем: ' + studentName)


# Тест на удаление студента
def test_delete_student():
    # Создаем запись
    studentName = "Иннокентий Смоктуновский"
    print('Создаем сущность Студент с именем: ' + studentName)
    new_student = Student(name=studentName, age=23)
    session.add(new_student)
    session.commit()

    # Удаляем запись
    student = session.query(Student).filter_by(name=studentName).first()
    session.delete(student)
    print('Удаляем сущность Студент с именем: ' + studentName)
    session.commit()

    # Проверяем удаление
    deleted_student = (
        session.query(Student)
        .filter_by(name=studentName)
        .first()
    )
    assert deleted_student is None
