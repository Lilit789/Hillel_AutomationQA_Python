lam_1 = lambda symbol, count=100: print(str(symbol) * int(count))

lam_1("sea", 5)
lam_1(5, 6)

print("__" * 100)  # to separate points of homework

lam_2 = lambda x, y: x if x > y else y

print(lam_2(8, 7))
print(lam_2(9, 10))

print("__" * 100)  # to separate points of homework

lam_3 = lambda: 10

print(lam_3())  
