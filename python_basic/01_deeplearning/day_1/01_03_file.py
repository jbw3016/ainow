# 1_3_file.py

# quiz
# poem.txt 파일에 들어있는 단어 갯수를 알려주세요

# review : read(), readline(), readlines(), split(), splitlines()

f = open(r"C:\Users\Harmony25\Desktop\DL\pythonProject\data\poem.txt", mode ='r', encoding='utf-8')

# print(poem.read())

words = 0
for line in f :
    print(line.strip().split())
    words += len(line.strip().split())
print(f"단어 수 : {words}")

f.close()