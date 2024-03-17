# 2_2_1_json.py
import json

# 문자열 -> 객체 (json.load()) : 전달받은 데이터(문자열 : character code)에 접근하기 위해 객체로 변환하여 사용
# 객체 -> 문자열 (json.dump()) : 사용한 데이터를 전달하기 위해 문자열(character code)로 변환하여 전송

j = '{"ip": "8.8.8.8"}'
print("j : ", j, type(j))

d = json.loads(j)
print("json.loads(j) : ", d, type(d))

# quiz 딕셔너리를 json 문자열로 변환

e = json.dumps(d)
print("json.dump(d) : ", e, type(e))


# 아래 데이터로부터 값에 해당하는 것만 출력하세요
dt = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''

dt_d = json.loads(dt)
print("\n1.")
print("time : ", dt_d["time"], type(dt_d["date"]))
print("milliseconds_since_epoch : ", dt_d["milliseconds_since_epoch"], type(dt_d["date"]))
print("date : ", dt_d["date"], type(dt_d["date"]))

print("\n2.")
for key in dt_d.keys():
    print(f"{key} : {dt_d[key]}, {type(dt_d[key])}")

print("\n3.")
for k in dt_d:
    print(k, dt_d[k], type(dt_d[k]))

dt_e = json.dumps(dt)