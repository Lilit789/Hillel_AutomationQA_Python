cortege = (1, 2, 3, 4, 5, 6, 7)
print(cortege[0:])

a1 = {1, 2, 3, 4, 5, 6, 7}
b1 = {5, 6, 7, 8, 9, 10, 11}

print("Set a1 is {}".format(a1))

print("Set b1 is {}".format(b1))

a1.add(0)
print("New version of a1 {}".format(a1))

c1 = a1.intersection(b1)
print("Try intersection command {}".format(c1))

d1 = a1.difference(b1)
print("Find difference between a1 and b1 {}".format(d1))

e1 = a1.symmetric_difference(b1)
print("What is is symmetric difference {}".format(e1))

