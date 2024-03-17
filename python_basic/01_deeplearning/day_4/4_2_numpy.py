# 4_2_numpy.py
import numpy as np

# a = np.arange(12).reshape(2, 3, 2)
# print(a)
# print()
#
# # 퀴즈
# # 2차원 배열의 마지막 요소 출력
#
# print(a[-1][-1])    # [] 역시 연산자이기 때문에 최소한으로 사용하는 것이 좋음
# print(a[-1, -1, -1])    # fancy indexing

b = np.arange(12).reshape(3, 4)
# 퀴즈
# 마지막 열만 출력
print(f"original b :\n{b}")
print()
print(f"b[:, -1] :\n{b[:, -1]}")
print()
print(f"b[-1:, :] :\n{b[-1:, :]}")
print()
print(f"b[:, -1:] :\n{b[:, -1:]}")
print("="*30)

print(np.zeros(3, dtype=np.int32))
print(np.zeros(3).astype(int))
print()

print(np.zeros((3, 4)).astype(int))
print(np.zeros((3, 4), dtype=np.int32))
print()

print(np.ones((3, 4)))
print(np.full((3, 4), fill_value=-1))
print("="*30)

c = np.zeros((5, 5), dtype=np.int32)
# print(c)

# 퀴즈
# 2차원 배열의 테두리를 1로 채워보시오
print(c)
print()
c[0], c[-1], c[:, 0], c[:, -1] = 1, 1, 1, 1
print(c)
print("="*30)

# 퀴즈
# 2차원 배열의 속을 2로 채워보시오
print("2차원 배열의 속을 2로 채워보시오")
c[1:-1, 1:-1] = 2
print(f"method 1 :\n{c}\n")
print("="*30)

# 퀴즈
# 2차원 배열의 대각선을 3로 채워보시오
print("2차원 배열의 대각선을 3로 채워보시오")
for i in range(len(c)):
    for j in range(len(c[0])):
        if i==j or i+j==4 :
            c[i][j] = 3
print(f"method 1 :\n{c}\n")

for i in range(len(c)):
    c[i][i] = 4
print(f"method 2 :\n{c}\n")

c[[range(5)], [range(5)]] = 5   # index array
print(f"method 3 :\n{c}\n")
print("="*30)

# 퀴즈
# 2차원 배열의 테두리를 0으로 인덱스 배열을 활용하여 채우기
print("2차원 배열의 테두리를 0으로 인덱스 배열을 활용하여 채우기")
c[[0, -1]], c[:, [0, -1]] = 0, 0
print(c)
print("="*30)

d1 = np.arange(12).reshape(3, 4)
d2 = np.arange(12).reshape(4, 3)
print(f"d1 is:\n{d1}\n")
print(f"d2 is:\n{d2}\n")
print(f"np.dot(d1, d2) is\n{np.dot(d1, d2)}\n")
print(f"transpose d1 is:\n{np.transpose(d1)}\n")
print(f"d1.T is:\n{d1.T}\n")
# difference between transpose and .T