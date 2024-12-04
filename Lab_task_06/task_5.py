class Product :
    def __init__(self, name, price) :
        self.name = name
        self.price = price

    def display_details(self) :
        print(f"Product Name : {self.name}")
        print(f"Product Price : {self.price}")


class Electronic_product(Product) :
    def __init__(self, name, price, warranty) :
        super().__init__(name, price)
        self.warranty = warranty

    def display_details(self):
        super().display_details()
        print(f"Warranty : {self.warranty}")

EP = Electronic_product("E_cycle", 50000, "1 year")
EP.display_details()