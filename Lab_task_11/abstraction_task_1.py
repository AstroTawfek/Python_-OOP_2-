from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("The car is roaring to life!")

    def stop(self):
        print("The car is coming to a smooth halt.")

class MotorCycle(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("The motorcycle is revving up!")

    def stop(self):
        print("The motorcycle is skidding to a stop.")


car = Car()
car.start()  # Call the start method for Car
car.stop()   # Call the stop method for Car


motorcycle = MotorCycle()
motorcycle.start()  # Call the start method for MotorCycle
motorcycle.stop()   # Call the stop method for MotorCycle

# Attempting to instantiate abstract class
try:
    vehicle = Vehicle()  # Raises TypeError
except TypeError as e:
    print(e)