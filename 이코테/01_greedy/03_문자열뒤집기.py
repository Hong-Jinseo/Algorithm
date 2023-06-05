# 그리디
# 문자열 뒤집기

s = input()
prev = s[0]
change = 0

# 숫자에 하나씩 방문하면서 0<->1 바뀌는 횟수 세기
for num in s:
    if prev != num:
        prev = num
        change += 1

print((change+1)//2)
