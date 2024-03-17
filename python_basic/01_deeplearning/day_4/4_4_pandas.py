# 4_4_pandas.py
import pandas as pd

# Series
print("Series\n")
s = pd.Series([1, 3, 5, 7])
print(s)
print()

print(f"s.index : {s.index}")
print(f"s.values : {s.values}")
print()

print(f"s[0] : {s[0]}")
print(f"s[3] : {s[3]}")
print()

s.index = ['a', 'b', 'c', 'd']
print(s)
print()

print(f"s['b'] : {s['b']}")
print("=" * 35)

# DataFrame
print("DataFrame\n")

data = {
    'city' : ['mokpo', 'mokpo', 'mokpo', 'busan', 'busan', 'busan'],
    'year' : [2021 , 2022, 2023, 2021, 2022, 2023],
    'population' : [300, 400, 350, 250, 300, 350]
}

df = pd.DataFrame(data)
print(df)
print()
df.index = list('abcdef')
print(df)
print()
print(f"df.columns : {df.columns}\n")
print(f"df.values : {df.values}\n")
print(f"city column data : {df['city']}\n")   # df[label name] 하면 column data를 불러옴
print(f"df.iloc[0] :\n{df.iloc[0]}\n")    # type은 Series
print(f"df.loc['a'] :\n{df.loc['a']}\n")
print(f"df.iloc[:3] :\n{df.iloc[:3]}\n")    # type은 DataFrame

# 퀴즈
# 부산 데이터만 출력
print(df.loc['d':'f'])  # df.loc의 경우 f도 포함
print(df.iloc[3 : 5])   # df.iloc의 경우 5는 포함하지 않음