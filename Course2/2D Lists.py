
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "burguer", "pasta"]
dessert = ["pudding", "cake"]

food = [drinks, dinner,dessert]
print(food)
print(food[1][2])

for i in food:
    for j in i:
        print(j, end=", ")