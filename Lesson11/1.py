class Car:
    def wheels(self):
        print("Number of wheels: 4")

    def mode_of_transport(self):
        print("Mode: private ")


class Bus:
    def wheels(self):
        print("Number of wheels: 4")

    def mode_of_transport(self):
        print("Mode: public")


car1 = Car()
bus1 = Bus()

vehicles = [car1, bus1]

for vehicle in vehicles:
    vehicle.wheels()
    vehicle.mode_of_transport()
    print()