# # 1_1_python.py
#
# # 1.
# print("hello " * 3)
#
# # 2.
# for _ in range(3) :
#     print("hello ", end = "")
# print("\n")
#
# # 3.
# a = "hello"
# print(a + " " + a + " " + a)
#
# # 4.
# a = []
# while 1 :
#     a.append("hello")
#     if len(a) == 3 :
#         break
# print(a)
#
# # 5.
# print("hello")
# print("hello")
# print("hello")
#
#
#
# print("chat gpt")
# print("chat gpt")
# print("chat gpt")
# print("chat gpt")
# print("chat gpt")
#
# # *****
# # *   *
# # *   *
# # *   *
# # *****
#
# a = "*"
# for i in range(5) :
#     for j in range(5) :
#         if i == 5 or i == 1 :
#             print(a * 5)

# 01234
# *   *
#  * *
#   *
#  * *
# *   *

for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()