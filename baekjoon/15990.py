# DP
# 1, 2, 3 더하기 5

import sys
input=sys.stdin.readline

DIV = 1000000009

t = int(input())

d = [[0, 0, 0] for _ in range(100001)]    # [1로 끝나는 조합 개수, 2로~, 3으로~]
d[1] = [1, 0, 0]    # 1
d[2] = [0, 1, 0]    # 2
d[3] = [1, 1, 1]    # 1+2, 2+1, 3

for i in range(4, 100001):
    # 1 작은 수 중, 2나 3으로 끝난 조합에 1 붙이기
    d[i][0] = (d[i-1][1] + d[i-1][2]) % DIV

    # 2 작은 수 중, 1이나 3으로 끝난 조합에 2 붙이기
    d[i][1] = (d[i-2][0] + d[i-2][2]) % DIV

    # 3 작은 수 중, 1이나 2로 끝난 조합에 3 붙이기
    d[i][2] = (d[i-3][0] + d[i-3][1]) % DIV

for _ in range(t):
    n = int(input())
    print(sum(d[n]) % DIV)
