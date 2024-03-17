# 07_02_softmax_regression_onehot.py

import pandas as pd
import numpy as np
from tensorflow import keras

x = [[1, 2],    # C
     [2, 1],    # C
     [4, 5],    # B
     [5, 4],    # B
     [8, 9],    # A
     [9, 8]]    # A
y = [[0, 0, 1],
     [0, 0, 1],
     [0, 1, 0],
     [0, 1, 0],
     [1, 0, 0],
     [1, 0, 0]]

model = keras.Sequential()  # functional() : 복잡한 형태의 신경망 조직 시에 사용
model.add(keras.layers.Dense(3))
    # Dense 내 뉴런의 갯수는 Label의 attribute 갯수
model.add(keras.layers.Activation("softmax"))
# model.add(keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.categorical_crossentropy, metrics="acc")

model.fit(x, y, epochs=100, verbose=1)

p = model.predict(x,verbose=0)
print(p)

# 퀴즈
# 에측한 결과에 대한 정확도를 구할 것.

# method 1
count = 0
for i in range(len(p)):
    if np.argmax(p[i]) == np.argmax(y[i]):
        count += 1
print(count / len(p))

# method 2
p_arg = np.argmax(p, axis=1)
print(p_arg)
y_arg = np.argmax(y, axis=1)
print(y_arg)
print(np.mean(p_arg == y_arg))