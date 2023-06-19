class example:
    def __init__(self):
        self._a = 8
        self.__a = 27


tup = example()

print(tup._a)
print(tup._example__a)