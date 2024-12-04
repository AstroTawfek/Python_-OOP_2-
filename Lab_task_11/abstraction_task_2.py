from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, details):
        self.brand = brand
        self.details = details

    @abstractmethod
    def ignite_engine(self):
        pass

    def halt_engine(self):
        print(f"The engine of {self.brand} has been halted.")

class Car(Vehicle):
    def __init__(self, brand, model, details):
        super().__init__(brand, details)
        self.model = model

    def ignite_engine(self):
        print(f"The engine of the {self.brand} {self.model} is now running.")

# Create an object of Car with a new instance name
my_car = Car("Toyota", "Tacoma", "Off-road pickup truck")
my_car.ignite_engine()

# Attempting to instantiate abstract class
try:
    vehicle = Vehicle("Generic", "Abstract Vehicle")
except TypeError as e:
    print(e)