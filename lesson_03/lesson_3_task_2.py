from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79111111111"),
    Smartphone("Apple", "iPhone 13", "+79222222222"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79333333333"),
    Smartphone("OnePlus", "9 Pro", "+79279444444444"),
    Smartphone("Google", "Pixel 6", "+79555555555")
 ]

for smartphone in catalog:
    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.phone_number}")
