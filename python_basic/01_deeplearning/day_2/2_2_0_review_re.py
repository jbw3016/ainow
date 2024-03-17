# 2_2_0_review_re.py

import re

db = '''3412    [|Bob|] 123
383-4  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
'''

# print(db)

# r : raw (r을 빼도 문제가 없지만, 패턴임을 명시하기 위해 사용)

# quiz 이름만 찾기

# print("1-1 : ", re.findall(r'[a-z|A-Z]+', db))    # 이 경우 |도 활용됨
# print("1-2 : ", re.findall(r'[A-Za-z]+', db))
# print("1-3 : ", re.findall(r'[A-Z][a-z]+', db))   # 대괄호에 의한 구분이 이루어짐
# print("1-4 : ", re.findall(r'[A-z]+', db))    # 아스키 코드를 안다면 문제가 생김 (대문자와 소문자 사이에 문자가 있음)
# print("1-5 : ", re.findall(r'[a-zA-Z]+', db))
#
# # quiz 번호만 찾기
#
# print("2-6 : ", re.findall(r'[0-9-]+', db))
# # print(re.findall(r'[0-9]+', db))의 작동 방식 : 3, 34, 341, 3412 : 이후에는 [0-9]+ 조건을 만족시키는 숫자가 없으니 끝

# quiz T로 시작하는 이름만 찾아보세요 / T로 시작하지 않는 이름만 찾아보세요
print("3-1-0 : ", re.findall(r'T[A-Za-z]+', db))
print("3-2-1 : ", re.findall(r'[A-Za-z]+', db))
print("3-2-2 : ", re.findall(r'[A-SU-Z][a-z]+', db))

# quiz T가 포함된 이름만 찾아보세요 / T가 포함되지 않는 이름만 찾아보세요
