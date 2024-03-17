# 3_1_open_hangul.py

# http://openhangul.com/nlp_ko2en   ?   q=%ED%95%98%EB%8A%98
# before ? : API (just regard as function)
# q : name of parameter
# after ? : data value

# quiz
# 오픈한글 사이트에서 한글 자판을 알파벳 자판으로 바꿔주는 서비스를 사용해서
# 특정 단어를 변환하는 코드 만들기

import requests, json, re

# input 키워드가 함수 안에 있는 것은 좋지 못함
# 함수 안 쪽에 print를 직접 사용하는 것보다 return을 사용하는 것이 좋음

# def kor_to_eng_1():
#     url_original = r"http://openhangul.com/nlp_ko2en"
#     A = input("변환할 한글을 입력하세요 : ")
#     print()
#
#     url = url_original + "?q=" + A
#
#     response = requests.get(url)
#     data = response.content.decode()
#
#     print("한글 : ", *re.findall(r'Result<br><br>> ([가-하]+)', data))
#     print("영어 : ", *re.findall(r'<img src="images/cursor.gif"><br>([A-Za-z]+)', data))

def kor_to_eng_2(hangul):
    url = r"http://openhangul.com/nlp_ko2en?q="+ hangul
    response = requests.get(url)
    data = response.content.decode()
    alpha = re.findall(r'<img src="images/cursor.gif"><br>([A-Za-z]+)', data)
    return alpha[0]

print(kor_to_eng_2("하늘"))
print(kor_to_eng_2("사랑"))
print(kor_to_eng_2("점심"))
print(kor_to_eng_2("김치찌개"))
print(kor_to_eng_2("컴퓨터"))
