# lambda parameters:expression

function = lambda x:x*2
print(function(5))

function2 = lambda x, y: x*y
print(function2(2,5))

function3 = lambda x, y, z: x+y+z
print(function3(1,2,3))

name = lambda first_name, last_name: "{} {} is living in london".format(first_name, last_name)
print(name("Joao", "Paulo"))

age_check = lambda age:True if age>=18 else False
print(age_check(121))

