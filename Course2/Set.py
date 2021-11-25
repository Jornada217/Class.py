
utensils = {"fork", "spoon", "knife"}
dishes = ["bowl", "plate", "soulsplat"]

furniture = {"cupboard", "sink", "fork"}
kitchen = [utensils, dishes, furniture]
utensils.add("napkin")
utensils.add("plate")
utensils.remove("plate")
print(kitchen)
for x in kitchen:
    for i in x:
        print(i, end=", ")
print()
#utensils.update(dishes, furniture)
dinner_today = utensils.union(dishes, furniture)
for y in dinner_today:
    print(y, end=", ")
print()
#What do furniture has, that dishes doesn't
print(furniture.difference(utensils))
