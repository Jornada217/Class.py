
class Duck:
    def walk(self):
        print("The duck walks")

    def swim(self):
        print("The duck swims")

    def eat(self):
        print("The duck eats")

class Chicken:
    def walk(self):
        print("The chicken walks")

    def swim(self):
        print("The chicken swims")

    def eat(self):
        print("The chicken eats")

class Person():
    def catch(self, Duck):
        duck.walk()
        duck.swim()
        duck.eat()
        print("You cought the animal")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)

#Walrus Operator
happy = True
print(happy)
print(name := "Joao Paulo")
print(age := 10)
print()
#Old method
food_list = list()
while True:
    food = input("What food do you like?: ").lower()
    if food == "end":
        break
    food_list.append(food)
print(food_list)
#Walrus
drinks_list = list()
while drinks := input("What do you like to drink?").lower() != "end":
    drinks_list.append(drinks)

