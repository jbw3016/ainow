# # 2_1_csv.py
#
# # 읽어서 2차원 리스트로 반환하는 함수
# f = open(r"C:\Users\Harmony25\Desktop\DL\pythonProject\data\us-500.csv", mode="r", encoding="utf-8")
#
# file_list = []
# for line in f:
#     file_list.append(line.strip().split(","))
#
# for i in range(len(file_list)):
#     for j in range(len(file_list[i])):
#         file_list[i][j] = file_list[i][j].strip("\"")
#
# print(file_list)
#
# print("\n==================================================================================\n")
#
# def read_us500_1():
#     f = open(r"C:\Users\Harmony25\Desktop\DL\pythonProject\data\us-500.csv", mode="r", encoding="utf-8")
#
#     for line in f:
#         print(eval(line.strip()))
#
#     f.close()
#
# read_us500_1()

# print("\n==================================================================================\n")
#
# def read_us500_2():
#     f = open(r"C:\Users\Harmony25\Desktop\DL\pythonProject\data\us-500.csv", mode="r", encoding="utf-8")
#
#     rows = []
#     for i, line in enumerate(f):
#         if i != 0:
#             # print(eval(line.strip()))
#             rows.append(list(eval(line.strip())))     # rows = [list(eval(line.strip())) for line in f]
#
#     f.close()     # with 구문 사용하면 생략 가능
#     return rows
#
# rows = read_us500_2()
# print(*rows[:3], sep="\n")

print("\n==================================================================================\n")

import csv

def read_us500_3():
    f = open(r"C:\Users\Harmony25\Desktop\DL\pythonProject\data\us-500.csv", mode="r", encoding="utf-8")

    rows = []
    f.readline()
    for items in csv.reader(f, delimiter=","):  #delimiter : 구획문자
        rows.append(items)

    f.close()
    return rows

rows = read_us500_3()
print(*rows[:3], sep="\n")

# csv.writer()