class Vehicle:
    def desc(self):
        print("General vehicle")

    def wheels(self):
        print("How many wheels? Unknown")


class Car(Vehicle):
    def desc(self):
        print("This is a car.")

    def wheels(self):
        print("How many wheels: 4")


class Bus(Vehicle):
    def desc(self):
        print("This is a bus.")

    def wheels(self):
        print("How many wheels: 4")


car1 = Car()
bus1 = Bus()

car1.desc()
car1.wheels()

bus1.desc()
bus1.wheels()