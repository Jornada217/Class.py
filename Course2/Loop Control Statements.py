
while True:
    name = input("Enter your name: ")
    if name != "":
        break
phone = "123-456-789"

for i in phone:
    if i == "-":
        continue
    print(i, end="")
print()
for i in range (1, 20+1):
    if i == 13:
        pass
    else:
        print(i, end=", ")
