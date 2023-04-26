class Car:
    def __init__(self, color, brand, city='Пермь'):
        self.color = color
        self.brand = brand
        self.engine = False
        self.city = city

    def start_engine(self):
        self.engine = True

    def finish_engine(self):
        self.engine = False

    def drive_to(self, city):
        if self.engine:
            if self.city == city:
                print("ЭЭЭ, да я уже тут!")
            else:
                print(f"Ехаем из {self.city} в {city}!")
                self.city = city
        else:
            print("Двигатель не заведен!")


car1 = Car("Зеленая", 'Toyota')
car1.drive_to('Столб')
car1.start_engine()
car1.drive_to('Столб')
car1.drive_to('Столб')
