class Address:
    def __init__(self, index, city, street, house, apartament):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartament = apartament

    def __str__(self):
        return f"{self.index} {self.city}, {self.street}",
        f"{self.house}, {self.apartament}"
