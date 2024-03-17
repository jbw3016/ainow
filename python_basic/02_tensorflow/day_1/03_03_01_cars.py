# 03_03_01_cars.py
# 딥러닝 모델 구축 후 속도가 30, 50 일 때의 제동거리를 구하시오

import pandas as pd
import numpy as np
from tensorflow import keras

file = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\cars.csv", index_col='Unnamed: 0')
    # 정답 데이터를 무엇으로 설정할 것인지 확인 필요
x_data = np.array(file["speed"]).reshape(-1, 1)
y_data = np.array(file["dist"]).reshape(-1, 1)
    # 도트 표기법 혹은 []를 활용해서 pandas의 column에 접근할 수 있다. (Series - 1차원)
    # df.values에 대한 fancy indexing을 활용해서 데이터 추출이 필요
    # (column이 많으면 column 인덱스로 추출이 어려움)
    # 일반적으로 fancy indexing을 활용하는 방법이 유용 (column이 여러개인 경우 합쳐야 하는 수고로움 적음)
print(f"x_data.shape : {x_data.shape}")
print(f"y_data.shape : {y_data.shape}\n")

# print(type(x_data))
model = keras.Sequential()
model.add(keras.layers.Dense(1))
model.compile(optimizer=keras.optimizers.SGD(0.0003),   # SGD(학습률)
              loss=keras.losses.mse)

model.fit(x_data, y_data, epochs=100, verbose=2)

print(model.evaluate(x_data, y_data))

z_data = np.array([[30], [50]])

print("predict\n")
print(model.predict(z_data))