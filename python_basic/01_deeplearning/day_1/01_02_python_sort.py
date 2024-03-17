# 1_2_python_sort.py
# difference between list.sort() sorted(list)

# a = [1, 24, 4, 32]
# print(" a : ", a)
# print("a.sort() : ", a.sort())
# print("after a.sort() : ", a)
#
# b = [23, 4, 344, 1]
# print("sorted(b) : ", sorted(b))
# print("after sorted(b) : ", b)

# sorted(b) : does not change its original list
# b.sort() : does change its original list

colors = ['red', 'green', 'Yellow', 'blue']
def to_lower(s):
    return s.lower()

# sorted(list, key) : key를 바탕으로 list를 정렬한다
print("print sorted(colors) : ", sorted(colors))
print("print sorted(colors, key=to_lower) : ", sorted(colors, key=to_lower))
print("print sorted(colors, key=to_lower, reverse = True) : ", sorted(colors, key=to_lower, reverse=True))