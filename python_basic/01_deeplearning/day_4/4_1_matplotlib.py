# 4_1_matplotlib.py
import random
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# quiz
# 100보다 작은 난수 100개로 구성된 x, y

def p4():
    x = [random.randrange(100) for _ in range(100)]
    y = [random.randrange(100) for _ in range(100)]
    plt.subplot2grid(shape=(3, 4), loc=(1, 0), rowspan=2)
    plt.plot(x, y, 'r>')
    plt.subplot2grid(shape=(3, 4), loc=(1, 1), rowspan=2)
    plt.plot(x, y, 'r>')
    plt.subplot2grid(shape=(3, 4), loc=(1, 2), rowspan=2)
    plt.plot(x, y, 'r>')
    plt.subplot2grid(shape=(3, 4), loc=(1, 3), rowspan=2)
    plt.plot(x, y, 'r>')
    plt.subplot2grid(shape=(3, 4), loc=(0, 0), colspan=2)
    plt.plot(x, y, 'r>')
    plt.subplot2grid(shape=(3, 4), loc=(0, 0), colspan=4, rowspan=3)
    plt.plot(x, y, 'r>')
    plt.show()

p4()

def p5():
    males = [30, 35, 27, 31, 37]
    males.sort()
    females = [29, 36, 37, 42, 19]
    females.sort()


# quiz
# females 그래프를 추가
# method 1
#     idx_m = range(0, len(males)*2, 2)
#     idx_f = range(1, len(females)*2, 2)
#     plt.bar(idx_m, males)
#     plt.bar(idx_f, females)
#     plt.show()

# method 2 : numpy를 활용
#     idx = np.arange(len(males))
#     print(idx)
#     plt.bar(idx, males, width=0.4)
#     plt.bar(idx+0.5, females, width=0.4)    # broadcasting 연산을 활용하는 것.
#     plt.show()

# method 3 subplot 으로 추가
    idx = range(len(males))
    plt.subplot(1, 2, 1)
    plt.bar(idx, males, width=0.7, label="age")
    plt.xlabel("age")
    plt.ylabel("idx")
    plt.title("Male")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.bar(idx, females, width=0.7, label="age")
    plt.xlabel("age")
    plt.ylabel("idx")
    plt.title("Female")
    plt.legend()
    plt.suptitle("<Age of Male and Female>")
    plt.show()
    sns.barplot(x=idx, y=males)
    plt.show()
p5()

# quiz
# 2016.gdp 파일 읽고 top10을 막대 그래프로 그리기
import csv

def get_top10():
    with (open(r"C:\Users\Harmony25\Desktop\LECTURE\01.DL_1\pythonProject\data\2016_GDP.txt", mode="r", encoding="utf-8") as f):
        f.readline()
        nation_list = []
        for line in f:
            _, n, d = line.strip().split(":")
            nation_list.append({n : int(d.replace(",", ""))})
        def get_dollars(nation):
            return list(nation.values())[0]
        sorted(nation_list, key=get_dollars)
        return nation_list[:10]

        # print(nation_list)
        # print(nation_list.keys())
        # for item in nation_list:

        # print(df)
print(get_top10())

def p6():
    n10, d10 = get_top10()
    print(n10)
    print(d10)