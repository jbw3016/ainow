# 0_quiz_answer.py

# hello 3번 출력 코드 5번
a = "hello"
print(a, a, a, sep = " ")
print(a*3)
print("hello hello hello")
print(a + a + a)
print(a), print(a), print(a)

# f_2 함수를 5가지 방식으로 호출
def f_2(a=0, b=0, c=0):
    print(a, b, c)

print("\ncall 1 : ", end="")
f_2()
print("call 2 : ", end="")
f_2(1, 2, 3)
print("call 3 : ", end="")
f_2(45, 55)
print("call 4 : ", end="")
f_2(a=12)
print("call 5 : ", end="")
f_2(a=12, b=34, c=45)

#   01234
# 0 *   *
# 1  * *
# 2   *
# 3  * *
# 4 *   *
n = 5
print("\n")
for i in range(n):
    for j in range(n):
        if i == j or (i + j) == (n - 1) :
            print("*", end = "")
        else : print(" ", end = "")
    print()

# 0~100 사이의 난수 10개로 이루어진 리스트 생성
import random

a = [random.randint(0, 100) for i in range(10)]
a = sorted(a)
print("\na : ", a)
b = [random.randrange(100) for _ in range(10)]
b = sorted(b)
c = [random.randrange(100) for i in range(10)]
c = sorted(c)

# 위 리스트를 거꾸로 출력
print("\nreverse a : ", a[::-1])
b.reverse()
print("reverse b : ", b)
print("reverse c : ", [c[i] for i in reversed(range(len(c)))])

# 위 리스트에서 홀수만 출력
print("\nodd number in a : ", [i for i in a if i % 2])
print("odd number in b : ", [i for i in b if i % 2])
print("odd number in c : ", [i for i in c if i % 2])

# colors를 글자 갯수 순으로 정렬
def to_lower(s):
    return s.lower()

colors = ['red', 'green', 'Yellow', 'blue']

def str_len(s):
    return len(s)

print(sorted(colors, key=str_len))
print(sorted(colors, key=lambda s : len(s)))
print(sorted(colors, key=len))

# 10000보다 작은 양수에 포함된 8의 갯수
total = 10000
target = '8'

result = [str(i).count(target) for i in range(total)]
print("method 1 : ", sum(result))

print("method 2 : ", str(list(range(total))).count(target))

n = 0
for i in range(total):
    for c in str(i) :
        n += c == target

print("method 3 : ", n)