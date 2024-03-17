# 01_01_pandas_movie_1.py

# primary_key : pk : make certain data as unique
# foreign_key : fk : pk from other file or realm
# normalizing : split data scale to prevent dataset so much larger

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
# print(users.head())
# print(ratings.head())
# print(movies.head())

movies = pd.merge(movies, pd.merge(users, ratings))
# print(movies)

# p1 = movies.pivot_table(values='Rating', index='Gender')

# 퀴즈
# 남녀 평균 평점을 구하시오

males = (movies["Gender"] == "M")
females = (movies["Gender"] == "F")
total_rating = movies["Rating"].mean()
males_rating = movies["Rating"][males].mean()
females_rating = movies["Rating"][females].mean()

print(f"전체 평점 : {total_rating}")
print(f"남자 평점 : {males_rating}")
print(f"여자 평점 : {females_rating}")

# female_mean = 0
# female_total_rate = 0
# female_count = 0
# male_mean = 0
# male_total_rate = 0
# male_count = 0
# for i in range(movies.shape[0]):
#     s = movies.iloc[i]
#     if s["Gender"] == "F":
#         female_count += 1
#         female_total_rate += s["Rating"]
#     else :
#         male_count += 1
#         male_total_rate += s['Rating']
# female_avr_rate = female_total_rate / female_count
# male_avr_rate = male_total_rate / male_count

# print(female_avr_rate, male_avr_rate)

# # method 1
# m_sum, m_cnt, f_sum, f_cnt, m_avr, f_avr, = 0, 0, 0, 0, 0, 0
# for g, r in zip(movies["Gender"], movies["Rating"]):
#     if g == "M":
#         m_sum += r
#         m_cnt += 1
#     else :
#         f_sum += r
#         f_cnt += 1
        
# m_avr = m_sum / m_cnt
# f_avr = f_sum / f_cnt
# print(m_avr, f_avr)