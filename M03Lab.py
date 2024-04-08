# Seneiya Cooke
# M03Lab.py
# accept user input for vehicle type & details then print them back in an easy tp read formant

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class AutoMobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_details(self):
        print(f"\nVehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

vehicle_type = input("Enter vehicle type (car, truck, plane, boat, broomstick): ").lower()    
print("\nPlease enter the details for your " + vehicle_type + ": ")
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Doors (2 or 4): ")
roof = input("Type of roof (solid or sun roof): ")

vehicle = AutoMobile(vehicle_type, year, make, model, doors, roof)

vehicle.display_details()