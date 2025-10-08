import requests
import os
from dotenv import load_dotenv
from conftest import get_base_url
token = 'Id7WO5JYHhRmuA8djo+D5zjIqW2LFGsuKbGS3XNBUcA6C7w6dJ+IREBK1+lDOX+6'


def get_company_info(token):
    try:
        base_url = get_base_url()

        headers = {
            'Authorization': f'Bearer {token}'
        }

        response = requests.get(
            f'{base_url}/company',
            headers=headers
        )

        if response.status_code == 200:
            company_data = response.json()
            company_id = company_data.get('id')
            return company_id
        else:
            raise Exception(
                f"Ошибка получения информации о компании: {response.text}"
            )

    except Exception as e:
        print(f"Произошла ошибка при получении company_id: {str(e)}")
        return None


if __name__ == "__main__":
    load_dotenv()

    token = os.getenv('YOUGILE_TOKEN')

    if not token:
        print("Токен не найден. Сначала получите токен через get_token.py")
    else:
        company_id = get_company_info(token)

        if company_id:
            print(f"Получен company_id: {company_id}")

            with open("touch.env", "a") as f:
                f.write(f"\nYOUGILE_COMPANY_ID={company_id}")
            print("Company ID сохранен в touch.env файл")
