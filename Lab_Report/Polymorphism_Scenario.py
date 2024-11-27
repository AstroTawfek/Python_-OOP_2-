"""
Scenario: 
A delivery company uses different modes of transportation for various packages, such
as Truck, Ship, and Plane. Each transport type has a different way of calculating the delivery
cost, which includes parameters like weight and distance.

Question:
Define a base class Transport with a method calculate_cost(weight, distance). Create three
derived classes Truck, Ship, and Plane, each implementing calculate_cost() differently based on
the transport mode. Demonstrate polymorphism by writing a function that calculates delivery
costs for each mode of transportation using a single list of transport objects.

"""

class Transport:
    def calculate_cost(self, weight, distance) :
        raise NotImplementedError("This method should be overridden in derived classes")

class Truck(Transport):
    def calculate_cost(self, weight, distance) :
        # Example cost calculation for Truck
        return weight * 1.5 + distance * 0.5

class Ship(Transport):
    def calculate_cost(self, weight, distance) :
        # Example cost calculation for Ship
        return weight * 1.2 + distance * 0.8

class Plane(Transport) :
    def calculate_cost(self, weight, distance) :
        # Example cost calculation for Plane
        return weight * 2.0 + distance * 1.5

def calculate_delivery_costs(transports, weight, distance) :
    costs = {}
    for transport in transports :
        costs[type(transport).__name__] = transport.calculate_cost(weight, distance)
    return costs

# Create a list of transport objects
transports = [Truck(), Ship(), Plane()]
    
# Define weight and distance for the delivery
weight = 100  # in kg
distance = 200  # in km
    
# Calculate delivery costs
delivery_costs = calculate_delivery_costs(transports, weight, distance)
    
# Print the delivery costs
for transport_type, cost in delivery_costs.items():
    print(f"The delivery cost using {transport_type} is : ${cost:.2f}")