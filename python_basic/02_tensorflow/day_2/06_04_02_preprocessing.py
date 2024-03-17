# 06_04_02_preprocessing.py

from sklearn import preprocessing
import numpy as np

cities = ['bali', 'paris', 'london', 'bali', 'london', 'prague', 'sydney']

# def label_encoder(cities):
#     enc = preprocessing.LabelEncoder()
#     result = enc.fit_transform(cities)
#     print(enc.classes_)
#     print(enc.classes_[result])
#     return result

# # enc.inverse_transform(result) : 숫자로 변환된 리스트를 cities 형태로 반환
# label_encoder(cities)

# # print(f"result : {label_encoder(cities)}")
# # print(f"type : {type(label_encoder(cities))}")

# # 퀴즈
# # inverse_transform 코드

# def label_binarizer(cities):
#     # 퀴즈
#     # cities 문자열 리스트를 LabelBinarizer 클래스를 사용해서 숫자로 변환
    
enc_1 = preprocessing.LabelEncoder()
result_fit_LE = enc_1.fit(cities)    # LabelEncoder() 객체 자체에 cities data 교육
print(f"enc_1.classes_ : {enc_1.classes_}")     # fit을 통해 입력된 cities data의 unique element를 보유하는 ndarray
result_transform_LE = enc_1.transform(cities)
print(f"result_transform_LE :\n{result_transform_LE}")
print()

enc_2 = preprocessing.LabelBinarizer()
result_fit_LB = enc_2.fit(cities)
print(f"enc_2.classes_ : {enc_2.classes_}")
result_transform_LB = enc_2.transform(cities)   # one-hot encoding : 0과 1을 사용하여 데이터를 변환
print(f"result_transform_LB :\n{result_transform_LB}")
print()

# 퀴즈
# print(result_transform_LB)을 print(result_transform_LE)로 변환 (one-hot-verctor => sparse)

inverse_class_1 = [list.tolist().index(1) for list in result_transform_LB]
inverse_class_2 = [np.argmax(list) for list in result_transform_LB]
inverse_class_3 = np.argmax(result_transform_LB, axis=1)    # 각 행에서 가장 큰 값의 인덱스를 반환

print("inverse_class_1")
print(inverse_class_1, type(inverse_class_1))
print()
print("inverse_class_2")
print(inverse_class_2, type(inverse_class_2))
print()
print("inverse_class_3")
print(inverse_class_3, type(inverse_class_3))
print()

# 퀴즈
# print(inverse_class_1)을 print(sparse_1)로 변환 (one-hot-verctor => sparse)

eye = np.identity(7, dtype=np.int32)
sparse_1 = eye[inverse_class_1]
print(sparse_1)