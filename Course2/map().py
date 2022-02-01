#Map function: Excecutes a function for each item as an iterable.

#Calculate the lenght of each word in the tupple

series = ('Joao', 'Paulo', 'Gomes', 'Grigoli')
def count(serie):
    return len(serie)
c = map(count, series)
print(c)
print(list(c))
print()

#Make a smoothie with the following:
fruits = ('Apple', 'Mango', 'Avocado')
blend = ('Milk', 'Whey', 'Water')
def smoothie(x, y):
    return x + ' with ' + y
c = map(smoothie, fruits, blend)
print(list(c))