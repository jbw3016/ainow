# 06_01_trees.py

# 퀴즈
# trees.csv 파일을 읽어서 Girth와 Height로 Volume을 예측하는 모델
# Girth가 10이고 Height가 70일때, 15이고 80일 때의 볼륨을 구할 것

import pandas as pd
import numpy as np
from tensorflow import keras

trees = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\trees.csv", index_col="rownames")

print(trees)
# groupby를 사용하면..?

x_data = trees.values[:, 0:-1]
y_data = trees.values[:,-1:]

model = keras.Sequential()
model.add(keras.layers.Dense(2))
model.compile(optimizer=keras.optimizers.SGD(0.0003),
              loss=keras.losses.mse)

model.fit(x_data, y_data, epochs = 1000, verbose=1)

print(model.evaluate(x_data, y_data))

test_data = np.array([10, 70, 15, 80]).reshape(-1, 2)

print(model.predict(test_data))