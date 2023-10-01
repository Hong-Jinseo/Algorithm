# DP
# 연속합

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]

for i in range(1, n):
    d[i] = max(array[i], d[i-1] + array[i])

# 시간초과 코드
# for i in range(1, n+1):         # i: 더하는 개수
#     for j in range(1, n-i+1):   # j: 더하는 범위(시작점)
#         d[i] = max(d[i], sum(array[j:j+i]))

print(max(d))
