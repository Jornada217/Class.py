#args
def add(*blah):
    sum = 0
    for i in blah:
        sum += i
    return sum

print(add(1))
print(add(1,2,3,4,5,6))
print()

#Kwargs
def hello(**blah):
    print("Hello",end=" ")
    for key,value in blah.items():
        print(value, end=" ")

hello(Highness="Our Highness", title="Mr", Name1="Joao", name2="Paulo", name3="Gomes", name4="Grigoli")