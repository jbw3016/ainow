# 4_3_songs.py

# 퀴즈
# 한국음악저작권협회에서 지드래곤의 저작권 정보를 가져오시오
import requests, re

result = []
def get_song(code, page):
    payload = {
        'S_PAGENUMBER': page,
        'S_MB_CD': code,
        }

    url = r"https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp"
    # response = requests.get(url)    # GET 방식으로 읽어옴을 의미
    # post 방식
    response = requests.post(url, data=payload)
    data = response.content.decode("utf-8")
# 퀴즈
# 저작물 정보를 깔끔하게 출력하세요
    t_body = re.findall(r'<tbody>(.+?)</tbody>', data, re.DOTALL)

    # print(t_body[1])
    # print("="*35)
    tr_body = re.findall(r'<tr>(.+?)</tr>', t_body[1], re.DOTALL)
    for line in tr_body:
        line = line.replace("<br/>", ",")
        line = re.sub(r' <img .+? />', '', line)
        data_1 = re.findall(r'<td>(.*?)</td>', line)    # 결측 데이터 확인
        data_1[0] = data_1[0].strip()
        print(data_1)

    return len(tr_body) > 0

# print(data_1)
# print(len(title))
# print(tr_body)

page = 1
while get_song('W0726200', page):
    print('-' * 10, page)
    page+= 1
