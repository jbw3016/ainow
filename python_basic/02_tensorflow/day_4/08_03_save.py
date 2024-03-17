# 08_03_save_model

from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn import preprocessing

def save_model(model_path):
    mnist = keras.datasets.mnist.load_data()
    (x_train, y_train), (x_test, y_test) = mnist

    x_train = x_train.reshape(-1, 784) / 255
    y_train = y_train.reshape(-1, 1)
    x_test = x_test.reshape(-1, 784) / 255
    y_test = y_test.reshape(-1, 1)

    model = keras.Sequential([
        keras.layers.Dense(10, activation='softmax') # (128, 10) / 60000, 10
    ])

    model.compile(optimizer=keras.optimizers.Adam(0.001),
                loss=keras.losses.sparse_categorical_crossentropy,
                metrics="acc")

    history = model.fit(x_train, y_train, epochs=10, verbose=2, validation_split=0.8, batch_size=100)


    e = model.evaluate(x_test, y_test, verbose=2)

    print(f"Evaluate : {e}")

    model.save(model_path)

def load_model(model_path):
    mnist = keras.datasets.mnist.load_data()
    (_, _), (x_test, y_test) = mnist

    x_test = x_test.reshape(-1, 784) / 255

    model = keras.models.load_model(model_path)
    print(f"Evaluate : {model.evaluate(x_test, y_test, verbose=0)}")

model_path = r'C:\Users\Harmony25\Desktop\Tensorflow\day_4\08_03_save_model\mnist.h5'

save_model(model_path)
load_model(model_path)