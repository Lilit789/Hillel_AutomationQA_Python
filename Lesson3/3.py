my_list = [1, 2, 3, 4, 5]
print(my_list)

new_my_list = my_list.copy()
new_my_list.append("apple")
print(new_my_list)

new_my_list.insert(1, "plums")
print(new_my_list)

my_list.pop(4)
print(my_list)

new_my_list.remove("apple")
print(new_my_list)

new_my_list.index(4)
print('The index of 4:', new_my_list.index(4))


my_list.extend(new_my_list)
print(my_list)

for x in new_my_list:
    my_list.append(x)
print(my_list)


