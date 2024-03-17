# 04_01_multiple_regression.py

import pandas as pd
import numpy as np
from tensorflow import keras

import numpy as np
from tensorflow import keras

x = np.array([1, 2, 2, 1, 4, 5, 5, 4, 8, 9, 9, 8]).reshape(-1, 2)
y = np.array([3, 3, 9, 9, 17, 17]).reshape(-1, 1)

model = keras.Sequential()  # functional() : 복잡한 형태의 신경망 조직 시에 사용
model.add(keras.layers.Dense(1))    # 뉴런이 1개인 Dense 층 (Fully connected layer)

model.compile(optimizer=keras.optimizers.SGD(0.005),
              loss=keras.losses.mse)

model.fit(x, y, epochs=1000, verbose=1)
print(model.evaluate(x, y))

# 퀴즈
# 2시간 공부하고 7번 출석한 학생과, 5시간 공부하고 1번 출석한 학생의 성적

test_data = np.array([2, 7, 5, 1]).reshape(-1, 2)
print(model.predict(test_data))