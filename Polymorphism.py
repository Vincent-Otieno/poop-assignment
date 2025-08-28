# The base class for all vehicles.
class Vehicle:
    """A base class for all vehicles."""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # The common move method.
    def move(self):
        """A generic method for movement."""
        print("This vehicle is moving.")

# A car subclass that inherits from Vehicle.
class Car(Vehicle):
    """A subclass for cars."""

    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    # The car's specific move method.
    def move(self):
        """The car's specific move method."""
        print(f"The {self.make} {self.model} is driving 🚗.")

# A plane subclass that also inherits from Vehicle.
class Plane(Vehicle):
    """A subclass for planes."""

    def __init__(self, make, model, max_altitude):
        super().__init__(make, model)
        self.max_altitude = max_altitude

    # The plane's specific move method.
    def move(self):
        """The plane's specific move method."""
        print(f"The {self.make} {self.model} is flying ✈️.")

# --- Program Execution ---

# A list containing different vehicle objects.
vehicles = [
    Car("Honda", "Civic", "Gasoline"),
    Plane("Boeing", "747", 45000),
    Car("Tesla", "Model 3", "Electric")
]

# A loop that calls the unique move() method for each vehicle.
for vehicle in vehicles:
    vehicle.move()

