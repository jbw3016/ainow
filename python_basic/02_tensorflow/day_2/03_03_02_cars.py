# 03_03_02_cars.py
# 딥러닝 모델 구축 후 속도가 30, 50 일 때의 제동거리를 구하고 예측 결과를 그래프로 그리시오

import pandas as pd
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

def read_cars():
    file = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\cars.csv", index_col='Unnamed: 0')
        # 정답 데이터를 무엇으로 설정할 것인지 확인 필요
    x = file.values[:, :-1]
    y = file.values[:, -1:]
        # df.values에 대한 fancy indexing을 활용해서 데이터 추출이 필요
        # (column이 많으면 column 인덱스로 추출이 어려움)
    # print(f"x_data.shape : {x.shape}")
    # print(f"y_data.shape : {y.shape}\n")
    return x, y

x, y = read_cars()
print(x)
print()
print(y)

model = keras.Sequential()
model.add(keras.layers.Dense(1))
model.compile(optimizer=keras.optimizers.SGD(0.0003),   # SGD(학습률)
              loss=keras.losses.mse)

model.fit(x, y, epochs=100, verbose=2)

print(model.evaluate(x, y))

z_data = np.array([[0], [30], [50]])    # [0]을 통해 bias 값 확인 가능,,,
print("predict\n")
print(model.predict(z_data))

plt.plot(x, y, 'ro')
plt.scatter(z_data, model.predict(z_data))
plt.plot(z_data, model.predict(z_data))
plt.xlabel("Speed")
plt.ylabel("Distance")
plt.show()