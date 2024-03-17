# 08_04_callback.py

from tensorflow import keras
import matplotlib.pyplot as plt

mnist = keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = mnist
x_train = x_train.reshape(-1, 784) / 255
x_test = x_test.reshape(-1, 784) / 255

model = keras.Sequential([
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer=keras.optimizers.RMSprop(0.001),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss',  # 뭘 monitor 하고 stopping 할 것인가?
                                               patience=10)     # 얼마나 참고 stopping 할 것인가?

reduce_lr = keras.callbacks.ReduceLROnPlateau(factor=0.2, patience=3)
    # factor : 학습률을 얼마나 감소시킬지를 결정하는 인자
    # patience : 성능이 향상되지 않은 상태를 얼마나 기다릴지를 결정하는 인자

checkpoints = keras.callbacks.ModelCheckpoint(  # 모델이 특정 조건에서 가장 좋은 성능을 보일 때 모델을 저장하는 역할
    filepath=r'C:\Users\Harmony25\Desktop\Tensorflow\day_4\08_03_save_model\mnist_{epoch:02d}-{val_loss:.5f}.h5',
    save_best_only=True,
    verbose=1
    )

history = model.fit(x_train, y_train, epochs=20, verbose=2, batch_size=100,
          validation_data=(x_test, y_test),
          callbacks=[checkpoints])

# print(history.history.keys())   # ['loss', 'acc', 'val_loss', 'val_acc']

print("loss :\n", history.history["loss"])
print("val_loss :\n", history.history["val_loss"])

# plt.subplots(nrows=2, ncols=2)
plt.subplot(1, 2, 1)
plt.title("loss")
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"], 'r')
plt.subplot(1, 2, 2)
plt.title("acc")
plt.plot(history.history["acc"])
plt.plot(history.history["val_acc"], 'r')
plt.show()

