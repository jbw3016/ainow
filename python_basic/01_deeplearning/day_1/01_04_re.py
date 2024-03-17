import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
'''

# print(db)

# r : raw (r을 빼도 문제가 없지만, 패턴임을 명시하기 위해 사용)
print(re.findall(r'[0-9]+', db))
