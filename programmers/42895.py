# DP
# N으로 표현

import sys
from itertools import product

input = sys.stdin.readline


def solution(N, number):
    if N == number:
        return 1

    # dp[i] = N을 i번 써서 만들 수 있는 수의 집합
    dp = [set() for i in range(N + 1)]
    dp[1].add(N)  # N

    for i in range(2, N + 1):
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            # 가능한 모든 연산
            for x, y in product(dp[j], dp[i - j]):
                dp[i].update({x + y, x - y, x * y})
                if y != 0:
                    dp[i].add(x // y)

        if number in dp[i]:
            return i

    return -1
