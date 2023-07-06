try:
    a = 0
    b = 0
    math = a / b
    print(math)
except ZeroDivisionError:
    print("Division by zero is impossible! Go to school!")

list = [1, 2, 3, 4, 7, "apple"]

try:
    list.append(7)
    list.remove("banana")
except ValueError:
    print("Value mistake!")
except IndexError:
    print("Index mistake!")
except Exception as mistake:
    print("Error:", mistake)
