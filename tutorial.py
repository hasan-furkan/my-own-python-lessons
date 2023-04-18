

class Car:
    
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color 
        
        
car1 = Car("Ford", "Mustang", 2023, "red")
print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.color)