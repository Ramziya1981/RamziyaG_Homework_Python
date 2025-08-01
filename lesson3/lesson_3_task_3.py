from address import Address
from mailing import Mailing


to_address = Address("123456", "Москва", "Улица Пушкина", "10", "5")
from_address = Address("654321", "Санкт-Петербург",
                       "Улица Лермонтова", "15", "7")
mailing = Mailing(to_address, from_address, 500, "TRK123456")

print(
    f"Отправление {mailing.track} из\n{mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"дом {mailing.from_address.house} - кв ",
    f"{mailing.from_address.apartament} в\n{mailing.to_address.index}, "
    f"{mailing.to_address.city}, {mailing.to_address.street},"
    f"дом{mailing.to_address.house} - кв ",
    f"{mailing.to_address.apartament}\n"
    f"Стоимость {mailing.cost} рублей."
)
