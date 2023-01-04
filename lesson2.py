# ClASSES and INSTANCES

class Personel:
    personel_number = 0
    zam_orani = 1.05
    def __init__(self, name, surname, price):
        self.name = name.title()
        self.surname = surname.title()
        self.price = price
        self.mail = f"{name.lower()}.{surname.lower()}@dev.com"
        
        Personel.personel_number += 1
        
    def get_full_name(self):
        return f"{self.name} {self.surname}" 
    
    def zam_uygula(self):
        # self.price = int(self.price * self.zam_orani) 
        self.price = int(self.price * Personel.zam_orani) 

print(Personel.personel_number)

per_1 = Personel("Hasan", "furkan", 40000)
per_2 = Personel("Hasan", "koprulu", 12000)
print(Personel.personel_number)

print(per_1.price)
per_1.zam_orani = 1.15
per_1.zam_uygula()
print(per_1.price)