
rows = int(input("How many rows?: "))
col = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(col):
        print(symbol, end="")
    print()