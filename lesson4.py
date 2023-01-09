
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
        

#### METHOD RESOLUTION ORDER
class Developer(Personel):
    zam_orani = 1.1
    
    def __init__(self, name, surname, price, prog_lang):
        super().__init__(name, surname, price)
        self.prog_lang = prog_lang
        

class Mudur(Personel):
    def __init__(self, name, surname, price, personeller = None):
        super().__init__(name, surname, price) 
        if personeller is None:
            self.personeller = []
        else:
            self.personeller = personeller
        
    def personel_ekle(self, per):
        if per not in self.personeller:
            self.personeller.append(per)
    
    def personel_sil(self, per):
        if per in self.personeller:
            self.personeller.remove(per)
            
    def personel_liste(self):
        for e, per in enumerate(self.personeller):
            e += 1
            print(e, per.get_full_name())
        

dev1 = Developer("Hasan", "furkan", 40000, "python")
dev2 = Developer("Hasan", "koprulu", 12000, "javascript")

# print(dev1.mail)
# print(dev2.mail)
# print(dev1.zam_orani)
# dev1.zam_uygula()
# print(dev1.zam_orani)

# print(dev1.mail)
# print(dev1.prog_lang)

mudur_1 = Mudur("Hasan", "furkan", 60000, [dev1])
mudur_2 = Mudur("Hasan", "furkan", 60000)

# print(mudur_1.get_full_name())
# print("----------------")
# mudur_1.personel_liste()
# print("----------------")
# mudur_1.personel_ekle(dev2)
# print("personel eklendi")
# mudur_1.personel_liste()
# print("----------------")
# mudur_1.personel_sil(dev1)
# mudur_1.personel_liste()

#isinstance
# print(isinstance(mudur_1, Mudur))
# print(isinstance(mudur_1, Personel))
# print(isinstance(mudur_1, Developer))

#issubclass
print(issubclass(Developer, Personel))
print(issubclass(Mudur, Personel))
print(issubclass(Mudur, Developer))