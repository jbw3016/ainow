# 1_2_python.py

# def f_1(a, b, c):
#     print(a, b, c)
#
# f_1(1, 2, 3)    # positional function call
# f_1(a=1, b=2, c=3)  # keyword function call (order does not matter.)

# def f_2(a = 0, b = 0, c = 0):
#     print(a, b, c)
#
# f_2()
# f_2(1, 1, 1)
# f_2(a = 1, b = 2, c = 3)
# f_2(1, 2)
# f_2(a = 3, b = 2)
# f_2(43, 43, c = 45)
# f_2(c = 495, b = 23, a = 55)

import random
a = []
for _ in range(10):
    a.append(random.randint(0, 100))
a= sorted(a)
print("a : ", a)

b = []
for _ in range(10):
    b.append(random.randrange(0, 100))
b= sorted(b)
print("b : ", sorted(b))

# list comprehension
c = sorted(random.randint(0, 100) for _ in range(10))
c= sorted(c)
print("c : ", c)

d = [random.randint(0, 100) for _ in range(10)]
d = sorted(d)
print("d : ", d)

# reversing
print("1. print reverse a : ", a[::-1])
b.reverse()
print("2. print reverse b : ", b)
print("3. print reverse c : ", end = "")
e = []
for i in reversed(range(len(c))) :
    e.append(c[i])
print(e)
print("4. print reverse d : ", end = "")
f = []
for i in range(len(d)-1, -1, -1):
    f.append(d[i])
print(f)

print(*[b[i] for i in reversed(range(len(b)))])



