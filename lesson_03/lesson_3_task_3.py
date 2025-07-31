from address import Adress
from mailing import Maling


address_from = Adress("123456", "Москва", "Тверская", "10", "25")
address_to = Adress("654321", "Санкт-Петербург", "Невский", "20", "12")


mailing = Maling(address_to, address_from, 500.00, "TRACK12345")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")