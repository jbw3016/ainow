# 4_5_movie.py

# primary_key : pk : make certain data as unique
# foreign_key : fk : pk from other file or realm
# normalizing : split data scale to prevent dataset so much larger

import pandas as pd

users = pd.read_csv(r"C:\Users\Harmony25\Desktop\DL_1\pythonProject\0.ml-1m\ml-1m\users.dat",
                    header=None,
                    delimiter='::',
                    engine='python',
                    names='UserID::Gender::Age::Occupation::Zip-code'.split('::'))
ratings = pd.read_csv(r"C:\Users\Harmony25\Desktop\DL_1\pythonProject\0.ml-1m\ml-1m\users.dat",
                      header=None,
                      delimiter='::',
                      engine='python',
                      names='UserID::MovieID::Rating::Timestamp'.split('::'))
movies = pd.read_csv(r"C:\Users\Harmony25\Desktop\DL_1\pythonProject\0.ml-1m\ml-1m\users.dat",
                    header=None,
                    delimiter='::',
                    engine='python',
                    names='MovieID::Title::Genres'.split('::'),
                    encoding='ISO-8859-1')
print(users.head())
print(ratings.head())
print(movies.head())

movies = pd.merge(movies, pd.merge(users, ratings))
print(movies)

p1 = movies.pivot_table(values='Rating', index='Gender')