# 05_01_activation_fuction.py

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1+np.e ** -z)

for z in np.linspace(-10, 10):  # 시작과 끝 사이에서 균등한 간격으로 지정된 개수의 값을 생성
    s = sigmoid(z)
    print("{:.5} : {:.2}".format(z, s))
    plt.plot(z, s, 'ro')

def softmax(z):
    z = np.e ** np.array(z)
    return z / np.sum(z)
    
plt.show()