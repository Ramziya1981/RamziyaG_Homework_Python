class Adress:
    def __init__(self, index, city, street, house, apartament):
        self.index = index
        self.citye = city
        self.street = street 
        self.house = house
        self.apartament = apartament
    def __str__(self):
        return f"{self.index} {self.city}, {self.street}, {self.house}, {self.apartament}"