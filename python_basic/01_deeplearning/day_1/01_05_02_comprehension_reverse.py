
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



