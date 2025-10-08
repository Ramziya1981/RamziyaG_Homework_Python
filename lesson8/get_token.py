import requests
import os
from dotenv import load_dotenv
from conftest import get_base_url
company_id = 'ba02d034-3aae-4014-a1ed-d7612ecf975c'
email = 'ramziyaginiyatullina19@gmail.com'
password = 'samBB2@5RqxW-im'
def get_auth_token(email, password, company_id):
    try:
        base_url = get_base_url()
        response = requests.post(
            f'{base_url}/auth/keys',
            json={
                'login': email,
                'password': password,
                'companyId': company_id  # Добавляем companyId в тело запроса
            }
        )
        
        if response.status_code == 201:
            token = response.json().get('key')
            return token
        else:
            raise Exception(f"Ошибка авторизации: {response.text}")
    
    except Exception as e:
        print(f"Произошла ошибка при получении токена: {str(e)}")
        return None

if __name__ == "__main__":
    load_dotenv()
    
    # email = os.getenv('YOUGILE_EMAIL') or input("Введите email: ")
    # password = os.getenv('YOUGILE_PASSWORD') or input("Введите пароль: ")
    
    # # Добавляем ввод companyId
    # company_id = os.getenv('YOUGILE_COMPANY_ID') or input("Введите companyId: ")
    
    token = get_auth_token(email, password, company_id)
    
    if token:
        print(f"Получен токен: {token}")
        
        with open("touch.env", "a") as f:
            f.write(f"\nYOUGILE_TOKEN={token}")
        print("Токен сохранен в touch.env файл")
