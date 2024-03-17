# 0_quiz.py
import random


# hello를 3번 출력하는 코드를 5개 만드세요

def f_2(a=0, b=0, c=0):
    print(a, b, c)

# f_2를 5가지 방식으로 호출해 보세요

# 0~100 사이의 난수 10개로 이루어진 리스트를 만드세요
list_1 = [random.randrange(100) for i in range(10)]
list_2 = [random.randint(0, 100) for _ in range(10)]
list_1.sort()
list_2.sort()
print(f"list_1 : {list_1}")
print(f"list_2 : {list_2}")
print()

# 리스트 b를 거꾸로 출력하세요 (3가지)
list_2.reverse()
print(f"reversed list_1 : {list_1[::-1]}")
print(f"reversed list_2 : {list_2}")
print()

# 리스트 b에서 홀수만 출력하세요
odd_list_1 = [item for item in list_1 if item % 2]
even_list_2 = [item for item in list_2 if item % 2 != 1]
odd_list_1.sort()
even_list_2.sort()
print(f"odd_list_1 : {odd_list_1}")
print(f"even_list_2 : {even_list_2}")
print()

# n과 m의 값을 바꾸세요
n, m = 5, 10
print(f"n = {n}, m = {m}")
n, m = m, n
print(f"n = {n}, m = {m}")


# colors를 대소문자 무시한 순서로 정렬하세요
colors = ['red', 'green', 'YELLOW', 'blue']

def to_lower(s):
    s.lower()
print(sorted(colors, key=to_lower))


# colors를 글자 갯수순으로 정렬하세요

# 10000보다 작은 양수에 포함된 8의 갯수는?

# poem.txt 파일에 들어있는 단어 갯수를 알려주세요

# us-500.csv 파일을 읽어서 2차원 리스트로 반환하는 함수를 만드세요 (csv 사용)

db = '''3412    [|Bob|] 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# 숫자만 찾아보세요
# 이름만 찾아보세요

# T로 시작하는 이름만 찾아보세요
# T로 시작하지 않는 이름만 찾아보세요

# url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
# response = requests.get(url)

# 기상청에서 읽어온 데이터로부터 code와 value만 예쁘게 출력하세요 (json 사용)

# 기상청에서 읽어온 데이터로부터 code와 value만 예쁘게 출력하세요 (정규표현식 사용)

url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
# location을 찾아보세요
# province를 찾아보세요
# city를 찾아보세요
# data를 찾아보세요
# data 안에 포함된 mode, tmEf, wf, tmn, tmx, rnSt를 찾아보세요

# kma.csv 파일을 2차원 리스트로 반환하는 함수를 만드세요

