
try:
    numerator = float(input("Enter a number to divide: "))
    denominator = float(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero.")
except ValueError as e:
    print(e)
    print("You can only divide by numbers.")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)