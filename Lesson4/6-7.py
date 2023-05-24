a = 4
b = 5
c = 6
z = 6

res = a & b  # AND with different numbers
print(res)
y = c & z  # AND with same numbers
print(y)

r = a ^ b   # XOR with different numbers
print(r)
e = c ^ z   # XOR with same numbers
print(e)

i = a | b  # OR with different numbers
print(i)
o = c | z   # OR with same numbers
print(o)

t = ~a  # NOT
print("Not is {}".format(t))

left_move1 = a << 1  # left move to one bit
print(left_move1)

left_move2 = a << 2 # left move to two bit
print(left_move2)

left_move3 = a << 3  # left move to tree bit
print(left_move3)

right_move1 = c >> 1  # right move to one bit
print(right_move1)

right_move2 = c >> 2  # right move to two bit
print(right_move2)

right_move3 = c >> 3  # right move to tree bit
print(right_move3)

string1 = "123456789".encode("utf-8")  # Counting the number of bytes in string1
print(len(string1))
string2 = "asdfgtrewcvbnmkhfd".encode("utf-8")   # Counting the number of bytes in string2
print(len(string2))

h = len(string1)  # assign the value of the number of bytes of the string1 to the variable
print(h)
u = len(string2)  # assign the value of the number of bytes of the string2 to the variable
print(u)

huAND = h & u  # AND
print(huAND)

huXOR = h ^ u  # XOR
print(huXOR)

huOR = h | u  # OR
print(huOR)

hNOT = ~ h   # NOT h
print(hNOT)