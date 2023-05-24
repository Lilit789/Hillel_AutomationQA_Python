import copy

list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = list1
list1.append(6)
print(list2)

test_shallow = [1, 2, 3, [1, 2, 3]]
test_copy = copy.copy(test_shallow)
print(test_shallow,  test_copy)

test_shallow[3] = 55
print(test_shallow, test_copy)


test_deep = [9, 85, 87]
test_try = copy.deepcopy(test_deep)
print(test_try)

test_deep[2] = 3
print(test_deep)
print(test_try)

