# 브루트 포스
# 1, 2, 3 더하기

t = int(input())

d = [0] * 13
d[1], d[2], d[3] = 1, 2, 4

for i in range(4, 13):
    d[i] = d[i-3] + d[i-2] + d[i-1]

for _ in range(t):
    n = int(input())
    print(d[n])
