# ClASSES and INSTANCES

class Personel:
    def __init__(self, name, surname, price):
        self.name = name.title()
        self.surname = surname.title()
        self.price = price
        self.mail = f"{name.lower()}.{surname.lower()}@dev.com"
        
    def get_full_name(self):
        return f"{self.name} {self.surname}" 


per_1 = Personel("Hasan", "furkan", 40000)
per_2 = Personel("Hasan", "koprulu", 12000)


# print(per_1.name)
# print(per_1.surname)
# print(per_1.price)
# print(per_1.mail)

print(per_1.get_full_name())