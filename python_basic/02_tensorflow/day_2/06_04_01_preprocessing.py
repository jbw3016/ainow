# 06_04_01_preprocessing.py

# 문자열 데이터의 숫자로의 변환

import numpy as np
from sklearn import preprocessing

cities = ['bali', 'paris', 'london', 'bali', 'london']

num_cities = []
for city in cities:
    num_cities.append(cities.index(city))
print(num_cities)

# .replace() : pandas 메서드

def encode(cities):
    uniques = sorted(set(cities))
    
    return [uniques.index(city) for city in cities]
    
print(encode(cities))