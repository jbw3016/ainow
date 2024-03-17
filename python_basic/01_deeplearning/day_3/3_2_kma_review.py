# find location
# find province
# find city
# find data
# find mode, tmEf, wf, tmn, tmx, rnSt in data

import requests, re

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
response = requests.get(url)
text = response.content.decode()

# print(text)

location = re.findall(r'<location wl_ver="3">(.+?)</location>', text, re.DOTALL)
# print("location :\n", location)

f = open(r'C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.csv', mode = 'w', encoding = "utf-8")

for loc in location:
    prov = re.findall(r'<province>(.+?)</province>', loc)
    city = re.findall(r'<city>(.+?)</city>', loc)
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)

    for datum in data:
        print(prov[0], city[0], *re.findall(r'<.+>(.+)</.+>', datum), sep = ",", file = f)
        # f.write(f"{prov[0]}{city[0]}{mode[0]}{tmEf[0]}{wf[0]}{tmx[0]}{tmn[0]}{rnSt[0]}") 형식으로 작성해도 됨

f.close()
        # sorted_data = prov[0],city[0], *re.findall(r'<.+>(.+)</.+>', datum)
        # print(sorted_data)

        # mode = re.findall(r'<mode>(.+)</mode>', datum)
        # tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        # wf = re.findall(r'<wf>(.+)</wf>', datum)
        # tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        # tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        # rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
        # print(mode, end=" ")
        # print(tmEf, end=" ")
        # print(wf, end=" ")
        # print(tmx, end=" ")
        # print(tmn, end=" ")
        # print(rnSt)

# quiz
# 앞에서 출력한 내용으로 kma.csv 파일을 만드세요.



# with open(r'C:\Users\Harmony25\Desktop\DL\pythonProject\day_3\kma.csv', mode = 'w', encoding = "utf-8") as file:
#     d