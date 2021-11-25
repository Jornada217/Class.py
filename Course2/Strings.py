#slicing, indexing
#[start:stop:step], where the start is inclusive and stop is exclusive.

name = "Joao Paulo Gomes Grigoli"
joke = "até cubana tem"
first_name = name[:10]
last_name = name[11:]
nick_name = name[::3]
reversed_name = name[::-1]
reversed_joke = joke[::-1]
print(first_name)
print(last_name)
print(nick_name)
print(reversed_name)
print(reversed_joke)
print()
#slice function
website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website1[slice])
print(website2.upper()[slice])

print("{0} reversed his name to {1}".format(name,reversed_name))
print("As he was confused, {1} reversed back his name change to {0}".format(name,reversed_name))
print()
text = "{} reversed his name to {}"
text2 = "As he was confused, {} reversed back his name change to {}"
print(text.format(name,reversed_name))
print(text2.format(reversed_name,name))