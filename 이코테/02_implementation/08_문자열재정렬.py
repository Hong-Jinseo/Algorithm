# 구현
# 문자열 재정렬

s = input()
alpha = list()
number = 0

for i in s:
    if i.isdigit():
        number += int(i)
    else:
        alpha.append(i)

alpha.sort()
result = ''.join(alpha)
result += str(number)

print(result)