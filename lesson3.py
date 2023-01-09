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
        self.price = int(self.price * self.zam_orani) 
        
    @classmethod
    def zam_oranini_belirle(cls, oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f"eski zam orani {eski_oran} guncellendi. yeni oran {cls.zam_orani}")
        
    @classmethod
    def from_string(cls, per_str):
        name, surname, price = per_str.split("-")
        return cls(name, surname, price)
    
    @staticmethod
    def mesai_gunleri(gun):
        if gun.weekday() == 5 or gun.weekday() == 6:
            return "hafta sonu"
        else:
            return "hafta ici"


per_1 = Personel("Hasan", "furkan", 40000)
per_2 = Personel("Hasan", "koprulu", 12000)

per_3 = "merhaba-helloworld-30000"

yeni_per_3 = Personel.from_string(per_3)
print(yeni_per_3.mail)
print(yeni_per_3.price)

# Personel.zam_oranini_belirle(1.1)
# print(Personel.zam_orani)
# print(per_1.zam_orani)
# print(per_2.zam_orani)

import datetime
tarih = datetime.date(2023,1,9)
print(tarih.day)
print(Personel.mesai_gunleri(tarih))