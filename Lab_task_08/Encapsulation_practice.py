class Vehicle:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def vehicle_info(self):
        print(f"Color : {self.__color}")


class Taxi(Vehicle):
    def __init__(self, color, brand, seats, fuel_type, model, capacity, variant):
        super().__init__(color)
        self.__brand = brand
        self.__seats = seats
        self.__fuel_type = fuel_type
        self.__model = model
        self.__capacity = capacity
        self.__variant = variant

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats):
        self.__seats = seats

    def get_fuel_type(self):
        return self.__fuel_type

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_variant(self):
        return self.__variant

    def set_variant(self, variant):
        self.__variant = variant

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Brand : {self.__brand}")
        print(f"Seats : {self.__seats}")
        print(f"Fuel Type : {self.__fuel_type}")
        print(f"Model : {self.__model}")
        print(f"Capacity : {self.__capacity}")
        print(f"Variant : {self.__variant}")


# Creating instances with new names and values
vehicle1 = Taxi("Red", "Audi A4", 4, "Petrol", "A4", 4, "Standard")
vehicle2 = Taxi("Black", "Toyota Highlander", 8, "Hybrid", "Highlander", 8, "Luxury")

# Accessing and modifying properties
vehicle1.set_brand("Audi A6")
vehicle1.set_model("A6")
vehicle1.set_capacity(5)
vehicle1.set_variant("Premium")

vehicle2.set_fuel_type("Electric")
vehicle2.set_model("Highlander XLE")
vehicle2.set_capacity(7)
vehicle2.set_variant("Hybrid")

# Displaying vehicle information
vehicle1.vehicle_info()
vehicle2.vehicle_info()