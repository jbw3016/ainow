# 03_01_linear_regression_2.py

# linear, multiple => regression
# logistic, softmax => classification

import numpy as np
from tensorflow import keras

x = np.array([1, 2, 3])
y = np.array([1, 2, 3])
z = np.array([5, 6, 7])

model = keras.Sequential()  # functional() : 복잡한 형태의 신경망 조직 시에 사용ㅋ
model.add(keras.layers.Dense(1))    # 뉴런이 1개인 Dense 층 (Fully connected layer)

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.mse)

model.fit(x, y, epochs=10)
print(model.evaluate(x, y))

print(model.predict(z))