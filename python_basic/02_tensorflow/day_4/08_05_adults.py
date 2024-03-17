# 08_05_adults.py

# 퀴즈
# adult.data 파일에 대해 모델을 구축하고 70% 학습, 30% 결과 도출
# LabelBinarizer 사용

import pandas as pd
import numpy as np
import keras
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

adult = pd.read_csv(r"C:\Users\Harmony25\Desktop\LECTURE\03.Tensorflow\data\adult\adult.data", header=None)

# 결측치를 어떻게 해결할 것인가? isnull.sum으로 해결되지 않는 것은?
# 숫자 데이터만 모은다
# 

# print(adult.shape)  (32561, 15)
# print(x_adult.shape)    (32561, 14)
# print(y_adult.shape)    (32561, 1)

# print(adult.head())
# print(adult.info())
x_adult = adult.values[:, :-1]
y_adult = adult.values[:, -1:]

# print(adult.info())

x_0 = preprocessing.scale(x_adult[:, 0]).reshape(-1, 1)
enc_x_1 = preprocessing.LabelBinarizer()
x_1 = enc_x_1.fit_transform(x_adult[:, 1]).reshape(-1, 9)
x_2 = preprocessing.scale(x_adult[:, 2]).reshape(-1, 1)
enc_x_3 = preprocessing.LabelBinarizer()
x_3 = enc_x_3.fit_transform(x_adult[:, 3]).reshape(-1, 16)
x_4 = preprocessing.scale(x_adult[:, 4]).reshape(-1, 1)
enc_x_5 = preprocessing.LabelBinarizer()
x_5 = enc_x_5.fit_transform(x_adult[:, 5]).reshape(-1, 7)
enc_x_6 = preprocessing.LabelBinarizer()
x_6 = enc_x_6.fit_transform(x_adult[:, 6]).reshape(-1, 15)
enc_x_7 = preprocessing.LabelBinarizer()
x_7 = enc_x_7.fit_transform(x_adult[:, 7]).reshape(-1, 6)
enc_x_8 = preprocessing.LabelBinarizer()
x_8 = enc_x_8.fit_transform(x_adult[:, 8]).reshape(-1, 5)
enc_x_9 = preprocessing.LabelBinarizer()
x_9 = enc_x_9.fit_transform(x_adult[:, 9]).reshape(-1, 1)
x_10 = preprocessing.scale(x_adult[:, 10]).reshape(-1, 1)
x_11 = preprocessing.scale(x_adult[:, 11]).reshape(-1, 1)
x_12 = preprocessing.scale(x_adult[:, 12]).reshape(-1, 1)
enc_x_13 = preprocessing.LabelBinarizer()
x_13 = enc_x_13.fit_transform(x_adult[:, 13]).reshape(-1, 42)

enc_y = preprocessing.LabelBinarizer()

x_data_scaled = np.concatenate((x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10, x_11, x_12, x_13), axis=1)
y_data_scaled = enc_y.fit_transform(y_adult).reshape(-1, 1)

print(x_data_scaled)
print(x_data_scaled.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x_data_scaled, y_data_scaled, test_size=0.33, random_state=42)

model = keras.Sequential(
    keras.layers.Dense(1, activation='sigmoid')
)
model.compile(optimizer=keras.optimizers.SGD(0.001),
              loss=keras.losses.binary_crossentropy,
              metrics="accuracy")

history = model.fit(x_train, y_train, verbose=2, epochs=10)

p = model.predict(x_train)
e = model.evaluate(x_test, y_test, verbose = 2)

print(f"prediction : {p}")
print(f"evaluation : {e}")
