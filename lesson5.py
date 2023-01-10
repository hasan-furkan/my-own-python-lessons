class Personel:
    zam_orani = 1.05
    def __init__(self, name, surname, price):
        self.name = name.title()
        self.surname = surname.title()
        self.price = price
        self.mail = f"{name.lower()}.{surname.lower()}@dev.com"
        
    def get_full_name(self):
        return f"{self.name} {self.surname}" 
    
    def zam_uygula(self):
        self.price = int(self.price * self.zam_orani) 
        
    def __repr__(self):
        return f"Personel('{self.name}', '{self.surname}', '{self.price}')"
        
    def __str__(self):
        return f"{self.get_full_name()} -- {self.mail}"
    
    def __add__(self, other):
        if isinstance(self, Personel):
            return self.price + other.price

    def __len__(self):
        return len(self.get_full_name())
 
 
"""
repr daha cok kod yazan kisiler icin. bu kodu 2000. satirda cagirdigi zaman anlayabilmesi icin.
repr ve str arasinda basit bir fark var. 
str ise son kullanicilar icin hazirlanmis olan DUNDER koddur.
""" 

        
per_1 = Personel("Hasan", "furkan", 40000)
per_2 = Personel("Hasan", "koprulu", 12000)

# print(per_1)
# print(str(per_1))
# print(repr(per_1))

# print(per_1.price + per_2. price)
print(per_1 + per_2)
# print(per_1.name, per_1.surname)
# print(len(per_1))