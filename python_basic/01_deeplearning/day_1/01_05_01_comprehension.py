# * star is for take off its type
#
# t = 1, 3, 5
# print(*t, sep = ", ")
# print(type(t))

import random

b = []
for _ in range(10):
    b.append(random.randrange(0, 100))
b= sorted(b)
print("b : ", b)

c = []
for i in b:
    if i % 2 != 0:
        c.append(i)
print("\nodd number in b : ", c)

# how to comprehend c?
ewww
print("comprehend version of c : ", d)

# double comprehension
#  method 1
result = []
for i in range(1, 10):
    for j in range(1, 3):
        result.append(i ** j)

print(result)
print(len(result))

# method 2
result = [i**j for i in range(10) for j in range(2)]