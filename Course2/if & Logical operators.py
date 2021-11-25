
age = int(input("What is your age?: "))
print("you are " + str(age) + " old.")

if age == 100:
    print("You are a century old.")
elif age > 100:
    print("You are over a century old.")
elif age >= 18:
    print("you are an adult!")
elif age <= 0:
    print("you haven't been born yet!")
else:
    print("You are a child!")

#Logical Operators

temp = float(input("What is the temperature outside?: "))

#if temp >= 0 and temp <= 30:
#    print("The weather is good today.")
#    print("Go outside!")
#elif temp <0 or temp > 30:
#    print("The weather is not so good. I recommend you to stay inside.")
# or you can use "not" statements to invert.

if not(temp >= 0 and temp <= 30):
    print("The weather is not so good. I recommend you to stay inside.")
elif not(temp <0 or temp > 30):
    print("The weather is good today.")
    print("Go outside!")