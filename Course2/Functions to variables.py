def hello():
    input("Hello")

# print(hello)
# hi = hello
# print(hi)
# hi()
# say = print
# say("Joao Paulo")

#Higher Order functions
#EX1
def quiet(text):
    return text.lower()

def loud(text):
    return text.upper()

def hello(func):
    text = func("Come here")
    print(text)
hello(loud)
hello(quiet)

#EX2
def divisor(x):
    def dividend(y):
        return y / x
    return dividend
divide = divisor(2)
print(divide(10))