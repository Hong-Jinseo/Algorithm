# 수학
# 소수 구하기

import sys
input = sys.stdin.readline


# 아라토스테네스의 체
def is_prime(num):
    array = [True] * (num+1)    # False면 소수가 아니라서 지워진 수
    array[0] = False
    array[1] = False

    for i in range(2, num+1):
        if array[i]:            # True라면 (소수라면)
            j = 2
            while i*j <= n:
                # 해당 소수의 배수들을 전부 지움
                array[i*j] = False
                j += 1
    return array


m, n = map(int, input().split())
lst = is_prime(n)

for i in range(len(lst)):
    if lst[i] and m <= i:
        print(i)


# # 시간초과 코드
# m, n = map(int, input().split())
# flag = True
#
# for target in range(m, n+1):
#     for i in range(2, target):
#         if target % i == 0:
#             flag = False
#     if flag:
#         print(target, end=' ')
#     flag = True
