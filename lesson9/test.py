from student import Student, Session


# Тест на добавление студента
def test_add_student():
    studentId = "1"
    print('Создаем сущность Студент с ID: ' + studentId)
    new_student = Student(
        user_id=studentId,
        level="Первый курс",
        education_form="Очная",
        subject_id=21
    )
    session = Session()
    session.add(new_student)
    session.commit()

    # Проверка добавления
    student = session.query(Student).filter_by(user_id=studentId).first()
    assert student is not None
    assert student.education_form == "Очная"

    # Удаляем за собой созданное
    student = session.query(Student).filter_by(user_id=studentId).first()
    session.delete(student)
    print('Удаляем сущность Студент с ID: ' + studentId)
    session.commit()
    session.close


# Тест на обновление студента
def test_update_student():
    # Сначала создаем запись
    studentId = "1"
    print('Создаем сущность Студент с ID: ' + studentId)
    new_student = Student(
        user_id=studentId,
        level="Первый курс",
        education_form="Очная",
        subject_id=21
    )
    session = Session()
    session.add(new_student)
    session.commit()

    # Обновляем данные
    student = session.query(Student).filter_by(user_id=studentId).first()
    student.education_form = "Заочная"
    session.commit()

    # Проверяем обновление
    updated_student = session.query(Student).filter_by(
        user_id=studentId
        ).first()
    assert updated_student.education_form == "Заочная"

    # Удаляем за собой созданное
    student = session.query(Student).filter_by(user_id=studentId).first()
    session.delete(student)
    print('Удаляем сущность Студент с ID: ' + studentId)
    session.commit()
    session.close


# Тест на удаление студента
def test_delete_student():
    # Сначала создаем запись
    studentId = "1"
    print('Создаем сущность Студент с ID: ' + studentId)
    new_student = Student(
        user_id=studentId,
        level="Первый курс",
        education_form="Очная",
        subject_id=21
    )
    session = Session()
    session.add(new_student)
    session.commit()

    # Удаляем за собой созданное
    student = session.query(Student).filter_by(user_id=studentId).first()
    session.delete(student)
    print('Удаляем сущность Студент с ID: ' + studentId)

    # Проверяем удаление
    deleted_student = (
        session.query(Student)
        .filter_by(user_id=studentId)
        .first()
    )
    assert deleted_student is None
    session.commit()
    session.close
