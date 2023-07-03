with open("Boney_M.txt", "w") as file:
    file.write("Ma ma ma ma\nMa Baker\nShe taught her four sons")

file = open("Boney_M.txt", "r")
content = file.read()
print(content)
file.close()

with open("Boney_M.txt", 'a') as file:
    file.write("\nFreeze I'm ma Baker\nPut your hands in the air and give me all your money")

file = open("Boney_M.txt", 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()

with open("Boney_M.txt", 'a') as file:
    while True:
        user_input = input("This is classic! You know exactly this song!: ")
        if user_input  == "Ma Baker":
            break
        file.write(user_input + "\n")
