# 2_3_json_kma.py

import requests, json, re

# url = 'https://www.naver.com/'
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'

response = requests.get(url)
print("1 : ", response)
# # print(response.text)
# print("2 : ", response.content)
#
text = response.content.decode()
print("print text : ", text)

#  quiz 기상청에서 읽어온 데이터로부터 코드와 value만 출력하시오.
# print(type(text))

# method 1
# text_dt = json.loads(text)
# for i in range(len(text_dt)):
#     for key in text_dt[i].keys():
#         print(f"{text_dt[i][key]} ", end="")
#     print()
# print('\n')

# method 2
# for item in text_dt:
#     print(item['code'], item['value'])
#
# text_out = json.dumps(text)

# quiz 기상청에서 읽어온 데이터로부터 코드와 value를 정규표현식을 사용하여 출력하시오.
# method 1
codes = re.findall(r'[0-9]+', text)
print("code : ", *re.findall(r'[0-9]+', text))
     # 과연 unique 한 값을 찾았는가? (만약 value 안에 11이 있다면..?)
     # 그러려면 주변의 unique 한 값과 함께 찾는 것이 필요
     # codes = re.findall(r'"code":"([0-9]+)"', text)
values = re.findall(r'"value":"([가-하]+)"', text)
print("value : ", *re.findall(r'"value":"([가-하]+)"', text))
print("\n")
for i in range(len(codes)):
    print(f"code : {codes[i]}, values : {values[i]}")     # zip 함수로 묶어서 사용하기

# method 2
print("\n")
cv = re.findall(r'"code":"([0-9]+)","value":"([가-하]+)"', text)

for c, v in cv:
    print(c,v)