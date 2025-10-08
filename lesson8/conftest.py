import requests
import os
import pytest
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_base_url():
    return "https://ru.yougile.com/api-v2"


BASE_URL = 'https://ru.yougile.com/api-v2'
TOKEN = os.getenv('YOUGILE_TOKEN')
COMPANY_ID = os.getenv('YOUGILE_COMPANY_ID')


@pytest.fixture
def session():
    session = requests.Session()
    session.headers.update({
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    })
    return session


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def created_project(session, base_url):
    project_name = f'TestProject_{datetime.now().strftime("%Y%m%d%H%M%S")}'
    data = {
        'name': project_name,
        'companyId': COMPANY_ID
    }
    response = session.post(f'{base_url}/projects', json=data)
    project = response.json()

    yield project

    # Очищаем созданный проект после теста
    try:
        session.delete(f'{base_url}/projects/{project["id"]}')
    except Exception as e:
        print(f"Ошибка при удалении проекта: {str(e)}")


@pytest.fixture
def invalid_token_session():
    session = requests.Session()
    session.headers.update({
        'Authorization': 'Bearer invalid_token',
        'Content-Type': 'application/json'
    })
    return session
