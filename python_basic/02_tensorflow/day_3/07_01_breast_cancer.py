# 07_01_breast_cancer.py

# 퀴즈
# wdbc.data 파일에 대해서 모델을 구축하고
# 7 : 3의 비율로 학습한 결과를 도출

import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

wdbc = open(r"C:\Users\Harmony25\Desktop\Tensorflow\data\wdbc.data")
# wdbc = pd.read_csv(r"C:\Users\Harmony25\Desktop\Tensorflow\data\wdbc.data", header=None,)

wdbc_file = []

for line in wdbc:
    wdbc_file.append(line.replace("\n", "").split(","))

wdbc_data = pd.DataFrame(np.array(wdbc_file))

x_data = wdbc_data.values[:, 2:].astype(float)
y_data = wdbc_data.values[:, 1]

enc = preprocessing.LabelEncoder()
enc.fit(y_data)
    # enc.fit()의 결과 enc.classes_ 의 리스트를 만듦.
    # enc.classes_를 바로 형성한다면, enc.fit() 없이 바로 enc.transform() 가능.
enc.classes_ = enc.classes_[::-1]
x_data_scaled = preprocessing.scale(x_data)
y_data_scaled = enc.transform(y_data).reshape(-1, 1)
print(y_data_scaled)

x_train, x_test, y_train, y_test = \
    train_test_split(x_data_scaled, y_data_scaled, test_size=0.30, random_state=42)

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation="sigmoid"))
model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy, metrics="acc")
    # 발생 확률을 따지는 y가 아니기 때문에 softmax를 사용하지 않음
model.fit(x_train, y_train, epochs=30, verbose=2, validation_data=(x_test, y_test))

wdbc.close()
