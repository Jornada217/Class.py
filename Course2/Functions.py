import math

pi = 3.14159
neg_pi = -3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(pow(neg_pi, 2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))
print()
#functions:

def hello(name1, name2):
    print("hello! "+name1)
    print("Hi "+name2)
hello("Joao", "Peter")

name3 = "Blah"
name4 = "Blah 2"
hello(name3, name4)
print()
#return Statement:

def multiply(num1, num2):
    return num1*num2
x = multiply(3,2)
print(x)

#Keyword arguments:

def hello(first,second,third,fourth):
    print("hello " + first + " " + second + " " + third + " " + fourth)

hello(second="Paulo",third="Gomes",fourth="Grigoli",first="Joao")

print("The number Pi is {}.".format(pi))
print("The number Pi is {:.2f}.".format(pi))
number = 1000
print("The number is {:,}.".format(number))
print("The number is {:b}.".format(number))
print("The number is {:x}.".format(number))
print("The number is {:e}.".format(number)) #Scientific notation