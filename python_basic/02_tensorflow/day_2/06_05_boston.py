# 06_05_boston.py

# 퀴즈
# boston.xls. 파일에 대한 모델을 구축하고
# 70% 학습, 30% 결과 도출
# 예측 결과가 정답과 가격이 얼마나 차이나는지 보일 것
# multiple linear-regression

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from sklearn import preprocessing

boston = pd.read_excel(r"C:\Users\Harmony25\Desktop\Tensorflow\data\boston.xls")

# print("boston.head()")
# print(boston.head())
# print()
# print("boston.info()")
# print(boston.info())
# print()
# print("boston.describe()")
# print(boston.describe())
# print()

x_train, x_test, y_train, y_test = \
    train_test_split(boston[:-1].values[:, :-1], boston[:-1].values[:, -1:], test_size=0.3, random_state=42)

print(boston.shape)
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

x_train_scaled = preprocessing.scale(x_train)
x_test_scaled = preprocessing.scale(x_test)

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation="sigmoid"))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.mse, metrics="mae")
model.fit(x_train_scaled, y_train, epochs=10, verbose=2, validation_data=(x_test_scaled, y_test))

pred_1 = model.predict(x_train_scaled)
pred_2 = model.predict(x_test_scaled)
eval_1 = model.evaluate(x_train_scaled, y_train)
eval_2 = model.evaluate(x_test_scaled, y_test)

# print(f"pred_1 : {pred_1}")
# print(f"pred_2 : {pred_2}")
print(f"eval_1 : {eval_1}")
print(f"eval_2 : {eval_2}")
print('mae : ', np.mean(np.abs(pred_2 - y_test)))