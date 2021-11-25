# sort() method = used with lists
# sort() function = used with iterables

students = ["Kennedy", "Richard", "Antonio", "Anderson"]
# students.sort()
for i in students:
    print(i)
print()
sorted_students = sorted(students)
for i in sorted_students:
    print(i)
print()
students.sort(reverse=True)
for i in students:
    print(i)
print()
# LEVEL 2
print("level 2")
student_data = [("Kennedy", "A", 20),
                ("Richard", "C", 18),
                ("Antonio", "B", 31),
                ("Anderson", "B+", 20),
                ("Pedro", "A", 17),
                ("Marco", "B", 36),
                ("Joao", "A", 35)]
friends_data = [("Luis", "A", 20),
                ("Paulo", "C", 18),
                ("Joao", "B", 19),
                ("yuri", "B+", 22)]
name = lambda names:names[0]  #This is saying what the colums are.
grade = lambda grades:grades[1]
age = lambda ages:ages[2]
student_data.sort(key=name, reverse=True)
for i in student_data:
    print(i)
print()
friends_data.sort(key=name)
for i in friends_data:
    print(i)
print()

# MAPS
print("MAPS")
store = [("shirt", 20.00),
         ("trouser", 25.00),
         ("jacket", 50.00),
         ("socks", 5.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_BRL = lambda data: (data[0], data[1]*5.5)
store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)
print()
store_BRL = list(map(to_BRL, store))
for i in store_BRL:
    print(i)
print()

# FILTER - Using the same list student_data
#filter(function, iterable)
print("FILTER")
age = lambda data: data[2] >= 20
adult_students = list(filter(age,student_data))
for i in adult_students:
    print(i)
print()

