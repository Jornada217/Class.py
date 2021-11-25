
#list comprehension
#list = [expression for item in iterable]
#list = [expression for item in iterable if conditional]
#list = [expression (if/else) for item in iterable]
squares = [i * i for i in range(1,11)]
print(squares)
print()
student_grades = [100, 93, 90, 81, 73, 67, 60, 57, 50, 40, 43, 0]
passed_students = [x for x in student_grades if x >= 60]
print(passed_students)
print()
passed_fail = [x if x >= 60 else "Failed" for x in student_grades]
print(passed_fail)
print()

#dictionary comprehension
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

cities_in_F = {"Maringa": 100, "Perino": 75, "Milano": 50, "London": 32}

cities_in_celsius = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_celsius)
print()

cities_weather = {"Maringa": "Sunny", "Perino": "Sunny", "Milano": "Smowing", "London": "Raining"}
cities_weather_sunny = {key: value for (key, value) in cities_weather.items() if value == "Sunny"}
print(cities_weather_sunny)
print()

cities_temperature = {key: ("warm" if value >= 20 else "cold") for (key,value) in cities_in_celsius.items()}
print(cities_temperature)
print()

def description(value):
    if value >= 30:
        return "HOT"
    elif value >= 20 < 30:
        return "Warm"
    else:
        return "Cold"
cities_temperature_desc = {key: description(value) for (key,value) in cities_in_celsius.items()}
print(cities_temperature_desc)
print()