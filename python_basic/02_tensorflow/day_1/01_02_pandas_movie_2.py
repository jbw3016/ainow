# 01_02_pandas_movie_2.py

import pandas as pd

users = pd.read_csv(r"C:\Users\Harmony25\Desktop\DL_1\pythonProject\0.ml-1m\ml-1m\users.dat",
                    header=None,
                    delimiter='::',
                    engine='python',
                    names='UserID::Gender::Age::Occupation::Zip-code'.split('::'))
ratings = pd.read_csv(r"C:\Users\Harmony25\Desktop\DL_1\pythonProject\0.ml-1m\ml-1m\ratings.dat",
                      header=None,
                      delimiter='::',
                      engine='python',
                      names='UserID::MovieID::Rating::Timestamp'.split('::'))
movies = pd.read_csv(r"C:\Users\Harmony25\Desktop\DL_1\pythonProject\0.ml-1m\ml-1m\movies.dat",
                    header=None,
                    delimiter='::',
                    engine='python',
                    names='MovieID::Title::Genres'.split('::'),
                    encoding='ISO-8859-1')

movies = pd.merge(movies, pd.merge(users, ratings))
print(movies.head())
print()

p1 = movies.pivot_table(values='Rating', index='Age', columns="Gender")
p2 = movies.pivot_table(values='Rating', index='Age', columns="Occupation")
p3 = movies.pivot_table(values='Rating', index=['Age', 'Gender'], columns='Occupation')
print(p1)
print(p2)
print(p3)