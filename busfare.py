# Parent class
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

# Child class
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage
bus = Bus(50)
print(f"Total Bus Fare: INR {bus.fare()}")
