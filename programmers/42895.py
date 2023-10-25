# DP
# N으로 표현

# 2차 풀이
from itertools import product

def solution(N, number):
    if N == number:
        return 1

    # dp[i] = N을 i번 써서 만들 수 있는 수의 집합
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(2, 9):
        # N을 i번 반복 나열한 경우
        dp[i].add(int(str(N) * i))

        # 사칙연산
        for j in range(1, i):
            for x, y in product(dp[j], dp[i - j]):
                dp[i].update({x + y, x - y, x * y})
                if y != 0:
                    dp[i].add(x // y)

        #
        if number in dp[i]:
            return i

    return -1
