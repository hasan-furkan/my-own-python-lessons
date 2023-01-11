# ClASSES and INSTANCES

class Personel:
    
    zam_orani = 1.05
    
    def __init__(self, name, surname, price):
        self.name = name.title()
        self.surname = surname.title()
        self.price = price
        
    @property    
    def mail(self):
        return  f"{self.name.lower()}.{self.surname.lower()}@dev.com"

    @property    
    def get_full_name(self):
        return f"{self.name} {self.surname}" 
    
    @get_full_name.setter
    def get_full_name(self, fullName):
        name, surname = fullName.split(" ")
        self.name= name
        self.surname = surname
    
    @get_full_name.deleter
    def get_full_name(self):
        print("degiskenler silindi")
        self.name = None 
        self.surname = None


per_1 = Personel("Hasan", "furkan", 40000)

per_1.get_full_name = "Furkan Koprulu"

print("--------")
print(per_1.name)
print(per_1.mail)
print(per_1.get_full_name)

del per_1.get_full_name

print(per_1.name)