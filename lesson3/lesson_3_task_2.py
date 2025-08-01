from smartphone import Smartphone


catalog = []

phone1 = Smartphone(brand="Apple", model="iPhone 12", number="+79123456789")
phone2 = Smartphone(brand="Samsung", model="Galaxy S21", number="+79234567890")
phone3 = Smartphone(brand="Google", model="Pixel 5", number="+79345678901")
phone4 = Smartphone(brand="OnePlus", model="8 Pro", number="+79456789012")
phone5 = Smartphone(brand="Xiaomi", model="Mi 11", number="+79567890123")

catalog.extend([phone1, phone2, phone3, phone4, phone5])


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
