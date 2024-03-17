# 07_04_soft_max_regression_sparse.py

import pandas as pd
import numpy as np
from tensorflow import keras

x = [[1, 2],    # C
     [2, 1],    # C
     [4, 5],    # B
     [5, 4],    # B
     [8, 9],    # A
     [9, 8]]    # A
y = [2, 2, 1, 1, 0, 0]  # 수정 포인트

model = keras.Sequential()  # functional() : 복잡한 형태의 신경망 조직 시에 사용
model.add(keras.layers.Dense(3))
    # Dense 내 뉴런의 갯수는 Label의 attribute 갯수
model.add(keras.layers.Activation("softmax"))
# model.add(keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.sparse_categorical_crossentropy, metrics="acc")     # 수정 포인트

model.fit(x, y, epochs=100, verbose=1)

p = model.predict(x,verbose=0)
print(p)

p_arg = np.argmax(p, axis=1)
print(p_arg)
print(np.mean(p_arg == y))
