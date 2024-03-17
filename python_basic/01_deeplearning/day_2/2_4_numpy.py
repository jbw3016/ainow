# 2_4_numpy.py

import numpy as np

# a = list("abcdefg")
# aa = np.array(a)
# aaa = np.array("abcdefg")
# # aaaa = np.array("a","b", "c", "d", "e", "f", "g")
# print("a : ", a, type(a))
# print("aa : ", aa, type(aa), aa.shape, aa.dtype, aa.size)
# print("aaa : ", aaa, type(aaa), aaa.shape, aaa.dtype, aaa.size)
# # print("aaaa : ", aaaa, type(aaaa), aaaa.shape, aaaa.dtype, aaaa.size)
# print()
#
# b = [i for i in range(12)]
# bb = np.arange(12)
# print("b : ", b, type(b))
# print("bb : ", bb, type(bb), bb.shape, bb.dtype, bb.size)
# print()
#
# print("+ operator : ", bb + 1)   # broadcast
# print("+ operator : ", bb + bb)  # vector
# print("* operator : ", bb * 2)
# print("* operator : ", 2 * bb)   # switching its order could be okay
# print("/ operator : ", bb / 5)
# print("// operator : ", bb // 5)
# print("% operator : ", bb % 5)
# print("> operator : ", bb > 5)
# print("<< operator : ", bb << 5)
# print("sin method : ", np.sin(bb))    # universal function
# print("add method : ", np.add(b, bb))
# print()
#
# c = bb.reshape(3, 4)    # same as bb.reshape(3, -1) or bb.reshape(-1, 4)
# print("reshape(3, 4) : ", c, type(c), c.shape, c.dtype, c.size)
# print()
#
# print("+ operator : ", c + 1)   # broadcast
# print("+ operator : ", c + c)  # vector
# print("* operator : ", c * 2)
# print("* operator : ", 2 * c)   # switching its order could be okay
# print("/ operator : ", c / 5)
# print("// operator : ", c // 5)
# print("% operator : ", c % 5)
# print("> operator : ", c > 5)
# print("<< operator : ", c << 5)
# print("sin method : ", np.sin(c))    # universal function
# print("add method : ", np.add(c, c))    # universal function
# print()

# quiz 2차원 배열을 1차원 배열로 변환 (3가지)
a = np.arange(12).reshape(3, 4)
print("2차원 배열 : ", a, type(a), a.shape, a.dtype, a.size)
print()

b_1 = a.reshape(12)
print("1차원 변환 결과_1 : ", b_1, type(b_1), b_1.shape, b_1.dtype, b_1.size)
b_2 = a.reshape(b_1.size)
print("1차원 변환 결과_2 : ", b_2, type(b_2), b_2.shape, b_2.dtype, b_2.size)
b_3 = a.reshape(-1)
print("1차원 변환 결과_3 : ", b_3, type(b_3), b_3.shape, b_3.dtype, b_3.size)
