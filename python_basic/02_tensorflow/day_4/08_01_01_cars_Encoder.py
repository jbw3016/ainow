# 08_01_01_cars_Encoder.py

# 퀴즈
# car.data 파일에 대해 동작하는 모델을 만드시오
# 7 : 3의 비율로 학습과 평가

import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

car_file = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\cars\car.data", header=None)
print(car_file.info())
print(car_file.nunique())

car_file.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'target']

# print(car_file.head())

car_x_data = car_file.values[:, :-1]
car_y_data = car_file.values[:, -1:]

# 내가 한 방법
enc_x_0 = preprocessing.LabelEncoder()
x_data_scaled_0 = enc_x_0.fit_transform(car_x_data[:, 0])
enc_x_1 = preprocessing.LabelEncoder()
x_data_scaled_1 = enc_x_1.fit_transform(car_x_data[:, 1])
enc_x_2 = preprocessing.LabelEncoder()
x_data_scaled_2 = enc_x_2.fit_transform(car_x_data[:, 2])
enc_x_3 = preprocessing.LabelEncoder()
x_data_scaled_3 = enc_x_3.fit_transform(car_x_data[:, 3])
enc_x_4 = preprocessing.LabelEncoder()
x_data_scaled_4 = enc_x_4.fit_transform(car_x_data[:, 4])
enc_x_5 = preprocessing.LabelEncoder()
x_data_scaled_5 = enc_x_5.fit_transform(car_x_data[:, 5])

# # LabelEncoder 한번에 하는 방법 01
# enc = preprocessing.LabelEncoder()
# features = []
# for i in range(6):
#     result = enc.fit_transform(car_x_data[:, i])
#     features.append(result)
# print("features")
# print(np.int32(features).T.shape)
# print("enc.classes_")
# print(enc.classes_)

# # LabelEncoder 한번에 하는 방법 02
# enc = preprocessing.LabelEncoder()
# features = [enc.fit_transform(xar_x_data[:, i]) for i in range(6)]
# features = np.int32(features).T

x_data_scaled = np.hstack((x_data_scaled_0, x_data_scaled_1, x_data_scaled_2, x_data_scaled_3, x_data_scaled_4, x_data_scaled_5))
x_data_scaled = x_data_scaled.reshape(-1, 6)

# print(x_data_scaled.shape) # (1728, 6)

enc_y = preprocessing.LabelEncoder()
y_data_scaled = enc_y.fit_transform(car_y_data)
# print(y_data_scaled.shape)  # (1728, 1)

# print(car_x_data.shape)   # (1728, 6)
# print(car_y_data.shape)   # (1728, 1)

x_train, x_test, y_train, y_test = train_test_split(x_data_scaled, y_data_scaled, test_size=0.3, random_state=42)

model = keras.Sequential()
model.add(keras.layers.Dense(4, activation='softmax'))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.sparse_categorical_crossentropy, metrics="acc")
history = model.fit(x_train, y_train, epochs = 50, verbose=2, validation_split=0.7)

p_1 = model.predict(x_train)
e_1 = model.evaluate(x_test, y_test)

print(f"평가 정확도 : {e_1[1]}")

# print(history)

# p_arg = np.argmax(p_1, axis =1)
# y_arg = y_train.flatten().astype(int)
# bools_w = p_arg != y_arg
# bools_r = p_arg == y_arg
# wrong = x_train[bools_w]
# right = x_train[bools_r]
# y_wrong, p_wrong = y_arg[bools_w], p_arg[bools_w]
# y_right, p_right = y_arg[bools_r], p_arg[bools_r]
# print("WRONG")
# print(enc_y.classes_[y_wrong])
# print(enc_y.classes_[p_wrong])
# print()
# print("RIGHT")
# print(enc_y.classes_[y_right])
# print(enc_y.classes_[p_right])
