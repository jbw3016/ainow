# 3_2_kma.py

import requests, json, re
url = r"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# quiz
# 기상청 주소로부터 province 데이터만 읽어오시오.
response = requests.get(url)
data = response.content.decode("utf-8")

# 만들어지지 않은 자기 자신의 리스트를 활용한 comprehension 코드는 작동하지 않는다.
# province = []
# for item in re.findall(r'<province>(.+)</province>', data):
#     if item not in province:
#         province.append(item)
#
# print("province is :")
# print(province)
# print(type(province), end="\n")

# # quiz
# # location을 찾기 (여러 줄에 걸쳐 있는 데이터 찾는 방법)
# # re.DOTALL : 여러 줄에 걸쳐 있는 데이터를 찾고자 할 때 사용 (개행문자를 무시)
# # .+ : greedy search
# #  /+? : non-greedy search

location = re.findall(r'<location wl_ver="3">(.+?)</location>', data, re.DOTALL)

# print(location)
# print("number of data :\n", len(re.findall(r'<location wl_ver="3">(.+?)</location>', data, re.DOTALL)))

# quiz
# location 속에서 province와 city 찾기
# for i in location:
#     print(f"{re.findall(r'<province>(.+)</province>', i)} : {re.findall(r'<city>(.+)</city>', i)}")

# quiz
# find 한번을 사용해서 찾아보기 (province와 city)


# for i in location:
#     print(i)
#     pov_1 = re.findall(r'<province>(.+)</province>\s+<city>(.+)</city>', i)
#     pov_2 = re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', i, re.DOTALL)
#     print(pov_1[0])
#     print(pov_2[0])
#     print()
#     break

# quiz
# 데이터 찾기
# for loc in location:
#     data= re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
# print(data, end="\n")
# print(len(data))

# quiz
# data 내 mode, tmEf, wf, tmn, tmx, rnSt 찾기
# mode, tmEf, wf, tmn, tmx, rnSt = [], [], [], [], [], []
# mode_1, tmEf_1, wf_1, tmn_1, tmx_1, rnSt_1 = [], [], [], [], [], []
# for loc in location:
#     prov = re.findall(r'<province>(.+)</province>', loc)
#     city = re.findall(r'<city>(.+)</city>', loc)
#     print(prov[0], city[0])
#     datas = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
#     mode_1, tmEf_1, wf_1, tmn_1, tmx_1, rnSt_1 = [], [], [], [], [], []
#     for data in datas:
#         mode_1 = re.findall(r'<mode>(.+?)</mode>', data)
#         tmEf_1 = re.findall(r'<tmEf>(.+?)</tmEf>', data)
#         wf_1 = re.findall(r'<wf>(.+?)</wf>', data)
#         tmn_1 = re.findall(r'<tmn>(.+?)</tmn>', data)
#         tmx_1 = re.findall(r'<tmx>(.+?)</tmx>', data)
#         rnSt_1 = re.findall(r'<rnSt>(.+?)</rnSt>', data)
#         print(mode_1[0], tmEf_1[0], wf_1[0], tmn_1[0], tmx_1[0], rnSt_1[0])
    # mode.append(mode_1)
    # tmEf.append(tmEf_1)
    # wf.append(wf_1)
    # tmn.append(tmn_1)
    # tmx.append(tmx_1)
    # rnSt.append(rnSt_1)

    # break

# print("tmEf : ", tmEf)
# print("wf   : ", wf)
# print("tmn  : ", tmn)
# print("tmx  : ", tmx)
# print("rnSt : ", rnSt)
# print("mode : ", mode)
# print()
#
# zipped_data = zip(tmEf_1, tmn_1, tmx_1, rnSt_1, mode_1)
# print([item for item in zipped_data])

# quiz
# mode 등등을 한번에 찾기
for loc in location:
    # print(loc)
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    print(prov[0], city[0])
    datas = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    for data in datas:
        items = re.findall(r'<.+>(.+)<.+>', data)
        print(items)


print(type(location))
    #     mode_1 = re.findall(r'<mode>(.+?)</mode>', data)
    #     tmEf_1 = re.findall(r'<tmEf>(.+?)</tmEf>', data)
    #     wf_1 = re.findall(r'<wf>(.+?)</wf>', data)
    #     tmn_1 = re.findall(r'<tmn>(.+?)</tmn>', data)
    #     tmx_1 = re.findall(r'<tmx>(.+?)</tmx>', data)
    #     rnSt_1 = re.findall(r'<rnSt>(.+?)</rnSt>', data)
    #     print(mode_1[0], tmEf_1[0], wf_1[0], tmn_1[0], tmx_1[0], rnSt_1[0])