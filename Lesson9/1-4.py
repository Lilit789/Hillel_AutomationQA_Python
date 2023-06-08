class empty:
    pass


empty = empty()
print(empty)

print("__" * 100)  # to separate points of homework


class Animal:

    def __init__(self, name):
        self.name = name

    def sayMeow(self):
        print("Meawwww! I'm a cat. My name is", self.name)

    dog = "Bod"

    @staticmethod
    def sayWoof():
        print("Woof! I'm a dog. My name is", format(Animal.dog))


cat = Animal("Tilda")
cat.sayMeow()
Animal.sayWoof()


class Puppy_and_Kitty(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)
        self.name = name

    def sayPiii(self):
        print("Piiii! We are puppy and kitty. Our names  are ", self.name)

name = Puppy_and_Kitty("Mikko and Grab")
name.sayPiii()


print("__" * 100)  # to separate points of homework