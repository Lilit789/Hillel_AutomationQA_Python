import abc
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class Cat(Animal):
    def abstract_method(self):
        print("Say Meow! I'm a cat")

class Kitty(Cat):
    def abstract_method(self):
        print("I'm a kitty")

class Dog(Animal):
    def abstract_method(self):
        print("Say Woof! Dog is here!")

obj1 = Cat()
obj1.abstract_method()

obj3 = Kitty()
obj3.abstract_method()

obj2 = Dog()
obj2.abstract_method()

print("__" * 100)  # to separate sections

class MatherMath(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def zxt(self):
        pass

class Math(MatherMath):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zxt(self):
        return int(self.x * self.x * self.y)

formul = Math(16, 50)
print("math example:", formul.zxt())


