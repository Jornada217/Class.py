
name = "joao paulo"

if(name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[0:4].upper()
last_name = name[5:].upper()
last_name_inv = name[-1:4:-1].upper()
print(first_name)
print(last_name)
print(last_name_inv)