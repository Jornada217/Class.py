# REDUCE
#reduce(function, iterable)

import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y:x + y, letters)
print(word)
print()

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y:x * y, factorial)
print(result)

#LIST COMPREHENSION
