class Car:

    weels = 4
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
    def drive(self):
        print("This {} is driving".format(self.model))
    def stop(self):
        print("This {} is stopped".format(self.model))

car1 = Car("Ford", "Mustang", "2021", "Green")
car2 = Car("GM", "Corvette", "2020", "Blue")
print(car1.model)
print(car2.colour)
car1.drive()
car2.stop()
print(Car.weels)
car2.weels = 2
print(car2.weels)

