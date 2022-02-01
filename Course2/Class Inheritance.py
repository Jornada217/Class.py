from abc import ABC,abstractmethod
class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
        return (self)
    def sleep(self):
        print("This animal is sleeping")
        return (self)
    def run(self):
        print("This animal is running")
        return (self)
    def __init__(self, weight, colour, skin):
        self.weight = weight
        self.colour = colour
        self.skin = skin

class Rabbit(Animal):
    def __init__(self, weight, colour, skin):
        super().__init__(weight, colour, skin)
class Canadian_Rabbit(Rabbit):
    def __init__(self, weight, colour, skin, eyes):
        super().__init__(weight,colour,skin)
        self.eyes = eyes
class Wild_Canadian_Rabbit(Canadian_Rabbit):
    def __init__(self, weight, colour, skin, eyes, ears):
        super().__init__(weight,colour,skin,eyes)
        self.ears = ears

class Fish(Animal):
    pass
class Hawk(Animal):
    pass

rabitt = Rabbit("10", "white", "hairy")
fish = Fish("1", "grey", "scales")
hawk = Hawk("3.5", "Black", "feather")
canadia_rabbit = Canadian_Rabbit
wild_canadian_rabbit = Wild_Canadian_Rabbit("11","brown", "light hair", "dark yellow", "long")

class Lunch(Rabbit, Fish):
    pass
class Supper(Fish, Hawk):
    pass
# lunch = Lunch()
# supper = Supper()

print(rabitt.alive)
print(fish.colour)
print(rabitt.skin)
fish.eat()
hawk.eat()
print(wild_canadian_rabbit.eyes)
print(wild_canadian_rabbit.ears)
print()
print(wild_canadian_rabbit.alive)
print()
rabitt.eat().sleep().run()
