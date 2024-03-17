# 08_02_02_multi_layers.py

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

model = keras.Sequential([
    # keras.layers.Input(shape=[784]),
        # model.fit 전에 summary를 보기 위한 방법
        # 데이터 1개의 shape을 적어야 함
    keras.layers.Dense(512, activation='relu'), # (784, 512) / 60000, 512
    keras.layers.Dense(256, activation='relu'), # (512, 256) / 60000, 256
    keras.layers.Dense(256, activation='relu'), # (256, 256) / 60000, 256
    keras.layers.Dense(128, activation='relu'), # (256, 128) / 60000, 128
    keras.layers.Dense(10, activation='softmax') # (128, 10) / 60000, 10
    # parameter의 갯수 = input의 feature 갯수 * 신경망 유닛의 수 + 편향(신경망 유닛의 수)
])

# # parameter 갯수
# a = 784*512 + 512   # 401,920
# 784개의 피처를 512개의 클래스로 분류함
# b = 512*256 + 256   # 131,328
# 512개의 피처를 256개의 클래스로 분류
# c = 256*256 + 256   # 65,792
# 256개의 피처를 256개의 클래스로 분류
# d = 256*128 + 128   # 32,896
# 256개의 피처를 128개의 클래스로 분류
# e = 128*10 + 10     # 1290
# 128개의 피처를 10개의 클래스로 분류

# print(a, b, c, d, e)
# print(a + b + c + d + e)    # 633,226

# model.summary()
# exit()  # exit을 해야 뒤에 모델 실행이 되지 않음.

model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics="acc")

history = model.fit(x_train, y_train, epochs=10, verbose=2, validation_split=0.8, batch_size=100)

model.summary()

# p = model.predict(x_train)
# e = model.evaluate(x_test, y_test, verbose=2)

# print(f"Predict : {p}")
# print(f"Evaluate : {e}")

# # self-quiz
# # 예측 값에서 뭐가 정답이고 뭐가 오답인지, 정답과 오답을 표현
# print(set(y_train.flatten()))
# p_arg = np.argmax(p, axis=1)
# print(p_arg)