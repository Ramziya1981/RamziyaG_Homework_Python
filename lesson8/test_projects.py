import json
import requests
import configparser

companyId = 'ba02d034-3aae-4014-a1ed-d7612ecf975c'
config = configparser.ConfigParser()
config.read('config.ini')
login = config['General']['login']
password = config['General']['password']

# Удаляем все ранее выданные ключи

def delete_keys(base_url):
    creds = {
        'login': login,
        'password': password,
        'companyId': companyId
    }

    # формируем запрос на получение списка ключей
    # https://ru.yougile.com/api-v2#/operations/AuthKeyController_search
    resp = requests.post(base_url + '/auth/keys/get', json=creds)
    print("строка json с данными по запросу о всех ключах", resp.json())
    # Загружаем строку в парсер json
    json_string = json.dumps(resp.json())
    data = json.loads(json_string)
    # проходим по всем объектам в json и берем значение key у каждого
    for key_info in data:
        print(key_info),
        # формируем запрос на удаление каждого полученного ранее ключа
        # https://ru.yougile.com/api-v2#/operations/AuthKeyController_delete
        resp = requests.delete(
            base_url + '/auth/keys/' + key_info['key'],
            json=creds
    )
    print("Ключ: " + key_info['key'] + " Результат удаления:" + resp.text)


# Получаем новый ключ

def get_key(base_url):

    creds = {
        'login': login,
        'password': password,
        'companyId': companyId
    }
    # формируем запрос на удаление каждого полученного ранее ключа
    # https://ru.yougile.com/api-v2#/operations/AuthKeyController_create
    resp = requests.post(base_url + '/auth/keys', json=creds)
    assert resp.json()["key"] is not None
    assert resp.status_code == 201
    print("Получен новый ключ: " + resp.json()["key"])
    return resp.json()["key"]


def test_create_project_positive(session, base_url):

    # Очистка существующих ключей
    delete_keys(base_url)

    # Получение нового токена
    token = get_key(base_url)
    print(token)
    # Проверка полученного токена
    assert token, "Токен не был получен"

    # Формируем заголовки с новым токеном
    headers = {
       "Authorization": f"Bearer {token}"
    }
    print("Authorization " f"Bearer {token}")
    # Подготавливаем данные для создания проекта
    project_data = {
        "title": "Ramziya: Positive Test Project"
    }

    # Выполняем запрос на создание проекта
    response = session.post(
        f"{base_url}/projects",
        json=project_data,
        headers=headers
    )

    # Проверяем статус ответа

    assert response.status_code == 201, (
        f"Ожидался статус 201, получен {response.status_code}"
    )

    # Проверяем содержимое ответа
    response_data = response.json()
    print(f"response: {response_data}")
    created_project = response_data["id"]
    assert "id" in response_data, "Отсутствует ID проекта"

    # Используем created_project в дальнейших проверках
    assert isinstance(created_project, str), "ID проекта должен быть строкой"
    print(f"Создан проект с ID: {created_project}")


# Тест на создание нового проекта (негативный)
# Невалидные данные - отсутствует обязательное поле title
def test_create_project_negative_1(session, base_url):
    delete_keys(base_url)
    token = get_key(base_url)
    headers = {"Authorization": f"Bearer {token}"}
    invalid_data = {
        "invalid": "Invalid project"
    }
    response = session.post(
       f"{base_url}/projects",
       json=invalid_data,
       headers=headers
    )
    # Проверки
    print(response.text)
    assert response.status_code == 400
    assert "title should not be empty" in response.json()["message"]

# Тест на создание нового проекта (негативный)
# Проверка с некорректным наименованием проекта
# (c браузера проект с именем ??? не завести)


def test_create_project_false_positive(session, base_url):
    delete_keys(base_url)
    token = get_key(base_url)
    headers = {"Authorization": f"Bearer {token}"}
    invalid_company_data = {
        "title": "???"
    }
    response = session.post(
        f"{base_url}/projects",
        json=invalid_company_data,
        headers=headers
    )
    print(response.text)
    assert response.status_code == 201
    assert "id" in response.json()


def test_update_project_positive(session, base_url):
    delete_keys(base_url)
    token = get_key(base_url)

    headers = {"Authorization": f"Bearer {token}"}
    
    # Сначала создаём проект
    project_data = {
        "title": "Test Project for Update"
    }
    create_response = session.post(
        f"{base_url}/projects",
        json=project_data,
        headers=headers
    )
    assert create_response.status_code == 201
    project_id = create_response.json()["id"]
    print(f"Создан проект с ID: {project_id}")

    headers = {"Authorization": f"Bearer {token}"}
    update_data = {
        "title": "???!!!&&&&"
    }
    response = session.put(
        f"{base_url}/projects/{project_id}",
        json=update_data,
        headers=headers
    )
    print(f"created_id {project_id}")
    print(response.text)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_update_project_negative(session, base_url):
    # Попытка обновить несуществующий проект
    delete_keys(base_url)
    token = get_key(base_url)
    headers = {"Authorization": f"Bearer {token}"}
    response = session.put(
        f"{base_url}/projects/999999",
        json={"title": "Несуществующий проект"},
        headers=headers
    )
    print(response.text)
    assert response.status_code == 404
    assert response.json()["message"] == "Проект не найден"
