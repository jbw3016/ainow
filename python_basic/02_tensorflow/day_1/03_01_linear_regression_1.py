# 03_01_linear_regression_1.py

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])  # input data
y = np.array([1, 2, 3])  # target data

# 사실상의 손실함수 (비용함수를 평균하지 않은 것 = 손실함수)
def cost(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        c += (hx - y[i]) ** 2
    return c

def show_cost():
    for i in range(-30, 50):
        w = i / 10
        plt.plot(w, cost(x, y, w), 'ro')
    plt.show()

def gradient_descent(x, y, w):
    c = 0
    for i in range(len(x)):
        hx = w * x[i]
        c += 2 * (hx - y[i]) * x[i]
    return c / len(x)

def show_gradient():
    for i in range(-30, 50):
        w = i / 10
        plt.plot(w, gradient_descent(x, y, w), 'ro')
    plt.show()
    
def show_gradient_2():
    w = -5
    for i in range(5):
        c = cost(x, y, w)
        g = gradient_descent(x, y, w)
        w -= 0.1 * g
        # print(i, c)
        
    print(w * 5, "\n", w * 7)
    
    
show_cost()
# show_gradient()
# show_gradient_2()

# 퀴즈
# x가 5와 7일 때의 결과를 구하시오.
# w 를 얻었다는 것