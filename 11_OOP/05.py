# Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy
# np. Samochód, Rower, Autobus, Ciężarówki. Dodaj opisy zgodne z tym jak te pojazdy są klasyfikowane.
# Jaki rodzaj dokumentu jest potrzebny, by kierować poszczegolnym pojazdem.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def pass_driving_licence(self):
        pass


class Car(Vehicle):
    def pass_driving_licence(self):
        return 'cat B'

    def __str__(self):
        return self.brand

class Bike(Vehicle):
    def pass_driving_licence(self):
        return 'bike card'

class Bus(Vehicle):
    def pass_driving_licence(self):
        return 'cat D'


car = Car('Renault')
print(car)
print(car.pass_driving_licence())

bike = Bike('Mars')
print(bike.pass_driving_licence())

bus = Bus('Volvo')
print(bus.pass_driving_licence())