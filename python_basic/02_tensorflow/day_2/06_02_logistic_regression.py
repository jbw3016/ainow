# 06_02_logistic_regression.py

import pandas as pd
import numpy as np
from tensorflow import keras

import numpy as np
from tensorflow import keras

x = [[1, 2],
     [2, 1],
     [4, 5],
     [5, 4],
     [8, 9],
     [9, 8]]
y = [[0],
     [0],
     [1],
     [1],
     [1],
     [1]]

model = keras.Sequential()  # functional() : 복잡한 형태의 신경망 조직 시에 사용ㅋ
model.add(keras.layers.Dense(1))    # 뉴런이 1개인 Dense 층 (Fully connected layer)
model.add(keras.layers.Activation("sigmoid"))
# model.add(keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy, metrics="acc")

model.fit(x, y, epochs=100, verbose=1)
# print(model.evaluate(x, y))

prediction = model.predict(x)
print(prediction)

# 퀴즈
# 예측한 결과에 대해 정확도를 구하세요
p_bool = np.int32((prediction > 0.5))
print(p_bool)
print(np.mean(p_bool == y))

# print(f"accuracy : {count / len(prediction)}")