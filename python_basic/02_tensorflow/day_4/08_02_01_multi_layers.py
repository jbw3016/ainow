# 08_02_01_multi_layers.py

from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn import preprocessing

mnist = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = mnist

x_train = preprocessing.minmax_scale(x_train.reshape(-1, 784))    # 이미지 파일은 무조건 스케일링 한다
y_train = y_train.reshape(-1, 1)
x_test = preprocessing.minmax_scale(x_test.reshape(-1, 784))    # 이 경우 선택된 데이터셋에서의 최대 최소를 기준으로 학습
y_test = y_test.reshape(-1, 1)

# # 위의 minmax_scale의 문제 극복하는 방법
# x_train = x_train / 255

# print(x_train.shape)  # (60000, 784)
# print(y_train.shape)  # (60000, 1)
# print(x_test.shape)  # (10000, 784)
# print(y_test.shape)  # (10000, 1)

# # 바꾸는게 의미가 없음 / binarizer로 하면?
# # enc = preprocessing.LabelEncoder()
# # y_train_scaled = enc.fit_transform(y_train)
# # y_test_scaled = enc.fit_transform(y_test)
# # print(y_train_scaled)
# # print(y_test_scaled)

model = keras.Sequential()
model.add(keras.layers.Dense(512, activation='relu')) 
    # activation 함수를 사용하지 않으면 선형 신경망의 연결에 불과
    # sigmoid 함수와 같이 입력 값을 0과 1사이의 값으로 출력시키게 되면, 역전파 과정에서 가중치 변경에 제한 받음
    # (sigmoid를 사용하게 되면, 층이 깊어지면서 gradient가 급격하게 vanishing 되는 문제 발생)
    # 특정 임계 값을 넘으면 그 값을 그대로 전달하는 relu 함수를 사용
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(10, activation="softmax"))

model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics="acc")

history = model.fit(x_train, y_train, epochs=10, verbose=2, validation_split=0.8)

# p = model.predict(x_train)
# e = model.evaluate(x_test, y_test, verbose=2)

# print(f"Predict : {p}")
# print(f"Evaluate : {e}")

# # self-quiz
# # 예측 값에서 뭐가 정답이고 뭐가 오답인지, 정답과 오답을 표현
# print(set(y_train.flatten()))
# p_arg = np.argmax(p, axis=1)
# print(p_arg)