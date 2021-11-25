
#zip(*iterables)
#It is a zip object, and you can convert to a list using list(zip(*iterables))
# you can convert to a dictionary using dict(zip(*iterables))
usernames = ["Joao", "Paulo", "Grigoli", "Gomes"]
passwords = ("Pass123", "G@mes", "L@m123!", "P@ass!#$$$$$")
login_dates = ["jan/2015", "oct/2019", "may/2020", "feb/2021"]

users = list(zip(usernames, passwords, login_dates))
for i in users:
    print(i)
print()

users_dict = dict(zip(usernames, passwords))
for key,value in users_dict.items():
    print(key + ": " + value)