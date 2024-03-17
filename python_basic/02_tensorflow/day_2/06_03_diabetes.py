# 06_03_diabetes.py

import pandas as pd
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

diabetes = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\diabetes.csv")

# 퀴즈
# diabetes.csv 파일에 대해 동작하는 딥러닝 모델을 만들고
# 70%의 데이터로 학습하고 30%에 대해 정확도를 구하시오 (함수처리해서도 가능)

# print("head")
# print(diabetes.head())
# print()
# print("info")
# diabetes.info()
# print()
# print("describe")
# print(diabetes.describe())
# print()
# print(diabetes.isnull().sum())

x_train, x_test, y_train, y_test = train_test_split(
    diabetes.values[:, :-1], diabetes.values[:, -1:], test_size=0.3, random_state=42)
# train_test_split을 쓰지 않는다면,,
# x_train, x_test = x[:train_size], x[train_size:]
# y_train, y_test = y[:train_size], y[train_size:]


# StandardScaler : 모든 값이 평균 0, 표준편차가 1인 정규분포로 변환
# MinMaxScaler : 최소값 0, 최대값 1로 변환
# RobustScaler : 중앙값 과 IQR(interquartile range): 25%~75% 사이의 범위 사용해 변환
x_train_scaled = preprocessing.robust_scale(x_train)
x_test_scaled = preprocessing.robust_scale(x_test)

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation="sigmoid"))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy, metrics="acc")
model.fit(x_train_scaled, y_train, epochs=30, verbose=2, validation_data=(x_test_scaled, y_test))

print()
evaluation_train = model.evaluate(x_train_scaled, y_train, verbose=2)
evaluation_test = model.evaluate(x_test_scaled, y_test, verbose=2)
# 정확도가 낮은 이유 : feature 별 데이터의 단위 편차가 크기 때문
# 정확도를 높이기 위해서는 feature 별 데이터의 단위를 통일하는 것이 필요 -> 스케일링 필요
prediction_test = model.predict(x_test_scaled)
print(np.mean((x_test_scaled > 0.5) == y_test))

# # 스케일 변환
# # StandardScaler : 모든 값이 평균 0, 표준편차가 1인 정규분포로 변환
# # MinMaxScaler : 최소값 0, 최대값 1로 변환
# # RobustScaler : 중앙값 과 IQR(interquartile range): 25%~75% 사이의 범위 사용해 변환
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()   # scaler 변수에 StandardScaler() 클래스 객체 할당

# train_scaled = scaler.fit_transform(train_input)
# test_scaled = scaler.fit_transform(test_input)
# print(f"train_scaled :\n{train_scaled}\n") # numpy.ndarray 변환 출력
# # print(f"test_scaled :\n{test_scaled}\n")
# # print(train_scaled[:,1].std()) # 0번째 열(Sex) 데이터 표준편차 1