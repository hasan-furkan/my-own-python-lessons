# ClASSES and INSTANCES

class Personel:
        
    def __init__(self, name, surname, price):
        self.name = name.title()
        self.surname = surname.title()
        self.price = price
        self.__zam_orani = 1.05
    
    def zam_uygula(self):
        self.price = int(self.price * self.__zam_orani)
        
    def __getZamOrani(self):
        return self.__zam_orani


per_1 = Personel("Hasan", "furkan", 40000)

# print(per_1.__zam_orani)
print(per_1.price)
per_1.zam_uygula()
print(per_1.price)
print(per_1.getZamOrani())
