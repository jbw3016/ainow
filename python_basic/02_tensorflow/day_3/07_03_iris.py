# 07_03_iris.py

import pandas as pd
import numpy as np
import random
from tensorflow import keras
from sklearn import preprocessing

# 퀴즈
# iris_onehot 파일 모델 구축 후 7 : 3 학습

iris_file = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\iris_onehot.csv")

train_set = int(150 * 0.7)

iris_train = iris_file.sample(train_set)
iris_test = iris_file.sample(150-train_set)
    # sample() : 데이터가 겹칠 위험도 있기 때문에, 원본데이터를 대상으로 np,random.shuffle()을 사용하는 것이 좋음
    # np.random.shuffle() 을 사용해도 좋음 :np.random.shuffle(iris_file.values)
    # indices = np.arange(len(x)), np.random.shuffle(indices)
    # 인덱스 배열 : x = x[indicies], y = y[indicies]
    # drop_duplicates() : df의 중복 row를 제거

x_train = iris_train.values[:, :4]
x_test = iris_test.values[:, :4]
y_train = iris_train.values[:, 4:]
y_test = iris_test.values[:, 4:]

x_train_scaled = preprocessing.scale(x_train)
x_test_scaled = preprocessing.scale(x_test)

# print(x_train_scaled.shape)
# print(y_train)

model = keras.Sequential()
model.add(keras.layers.Dense(3, activation="softmax"))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.categorical_crossentropy, metrics="acc")
model.fit(x_train_scaled, y_train, epochs=100, verbose=2)

p_1 = model.predict(x_train_scaled)
# p_2 = model.predict(x_test_scaled)
evl_1 = model.evaluate(x_test_scaled, y_test, verbose = 2)

print(evl_1[1] * 100)

# print(p_1)

