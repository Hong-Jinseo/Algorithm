# 그리디
# A와 B

# s를 t로 바꿈
s = input()
t = list(input())

'''
t -> s

t 맨 뒤에서 A 제거
t 맨 뒤에서 B 제거 & 뒤집
'''

for i in range(len(t) - len(s)):
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()

if s == ''.join(t):
    print(1)
else:
    print(0)
