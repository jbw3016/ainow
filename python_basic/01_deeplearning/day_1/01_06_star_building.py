# *   *
#  * *
#   *
#  * *
# *   *

# 별을 출력하거나 출력하지 않는다는 관점.
# 규칙을 찾는 것에 관한 의미

for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#   01234
# 0 *****
# 1 *   *
# 2 *   *
# 3 *   *
# 4 *****

n = 5
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n, end="")
    else :
        for j in range(n) :
            if j == 0 or j == n-1:
                print("*", end="")
            else :
                print(" ", end="")
    print()

n = 5
for i in range(n):
    for j in range(n) :
        if i == 0 or i == 4 or j == 0 or j == 4:  # same as ; i % 4 == 0 and j % 4 == 0
            print("*", end="")
        else :
            print(" ", end="")
    print()

#   01234
# 0 *****
# 1 * * *
# 2 * * *
# 3 * * *
# 4 *****

n = 9
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n, end="")
    else :
        for j in range(n) :
            if j == 0 or j == n - 1 or j == n // 2:
                print("*", end="")
            else :
                print(" ", end="")
    print()