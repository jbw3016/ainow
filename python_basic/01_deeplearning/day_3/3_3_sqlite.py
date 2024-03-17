# 3_3_sqlite.py

# purpose : 텍스트 파일과 DB의 차이점 확인
# CRUD : Create, Read, Update, Delete

import sqlite3, csv

# quiz
# kma.csv 파일을 2차원 리스트로 반환하는 함수를 만들 것

def read_kma() :
    with open(r"C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.csv", mode='r', encoding='utf-8') as f:
        return [line.strip().split(",") for line in f]

        # csv_reader = csv.reader(f, delimiter=",")
        # return [line for line in csv_reader]

def create_db():
    conn = sqlite3.connect(r"C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.sqlite3")
    cursor = conn.cursor()

    query = "CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)"
    cursor.execute(query)

    conn.commit()
    conn.close()

def insert_row(row):
    conn = sqlite3.connect(r"C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.sqlite3")
    cursor = conn.cursor()

    # quiz
    # row에 들어있는 데이터를 전달

    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    query = base.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    cursor.execute(query)

    conn.commit()
    conn.close()

    # quiz
    # insert_all 함수를 만드시요.
def insert_all(rows):
    conn = sqlite3.connect(r"C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.sqlite3")
    cursor = conn.cursor()

    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    for row in rows:
        query = base.format(*row)
        cursor.execute(query)

    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect(r"C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.sqlite3")
    cursor = conn.cursor()

    rows = []
    query = "SELECT * FROM kma"
    for r in cursor.execute(query):
        rows.append(r)

    # conn.commit()     # 단순 불러오는 것이기 때문에 commit을 할 필요가 없음
    conn.close()

    return rows

# create_db()

rows = read_kma()
# print(rows)
# print()
# for row in rows:
#     insert_row(row)
insert_all(rows)

rows = fetch_all()
# print(rows)

# quiz
# 원하는 city의 날씨 데이터를 반환하는 함수를 만드시오.

def search_city(city):
    conn = sqlite3.connect(r"C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.sqlite3")
    cursor = conn.cursor()

    rows = []
    query = f'SELECT * FROM kma WHERE city ="{city}"'
    for r in cursor.execute(query):
        rows.append(r)

    conn.commit()
    conn.close()

    return rows

print()
print(search_city('서귀포'), sep="\n")
print(search_city('울릉도'), sep="\n")
print(search_city('울진'), sep="\n")
