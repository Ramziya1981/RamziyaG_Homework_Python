import requests
import os
import pytest
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

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

