# 수학
# 골드바흐의 추측

import sys
input = sys.stdin.readline

# 아라토스테네스의 체
MAX = 1000000

array = [True] * (MAX + 1)
array[0] = False
array[1] = False

for i in range(2, MAX + 1):
    if array[i]:
        j = 2
        while i*j <= MAX:
            array[i*j] = False
            j += 1


while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        if array[i] and array[n-i]:
            print(n, '=', i, '+', n-i)
            break
