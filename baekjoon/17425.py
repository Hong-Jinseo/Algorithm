# 수학
# 약수의 합

import sys
input = sys.stdin.readline

MAX = 1000000

d = [1] * (MAX+1)   # i의 약수의 합
s = [0] * (MAX+1)   # i까지의 모든 수의 약수의 합 (누적)
s[1] = 1

for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        # i의 배수에 값 추가
        d[i*j] += i
        j += 1

    s[i] = s[i-1] + d[i]

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    result.append(s[n])
print('\n'.join(map(str, result)))

