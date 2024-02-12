
# Module 6: Object-Oriented Programming - Example Script

# Classes and Objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def describe_car(self):
        return f'{self.brand} {self.model}'

car1 = Car('Toyota', 'Corolla')
print(car1.describe_car())

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    # Polymorphism (Method Overriding)
    def describe_car(self):
        description = super().describe_car()
        return f'{description} with a {self.battery_size} kWh battery'

electric_car1 = ElectricCar('Tesla', 'Model S', 75)
print(electric_car1.describe_car())

# Encapsulation - Demonstrated by accessing public methods and attributes while the internal representation of the object is hidden
print(f'Accessing public attribute directly: {electric_car1.battery_size} kWh')
# Note: For full encapsulation, use private attributes/methods and provide public methods for access
