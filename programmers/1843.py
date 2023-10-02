# DP
# 사칙연산

def solution(arr):

    num, ops = [], []
    for idx, element in enumerate(arr):
        if not idx % 2:
            num.append(int(element))
        else:
            ops.append(element)

    n = len(num)

    # dp[i][j] = i부터 j까지의 최댓값/최솟값
    max_dp = [[int(-1e9)] * n for _ in range(n)]
    min_dp = [[int(1e9)] * n for _ in range(n)]

    for scope in range(n):
        for start in range(n - scope):
            end = start + scope

            # 숫자가 1개라면
            if start == end:
                max_dp[start][end] = min_dp[start][end] = num[start]
                continue

            for pivot in range(start, end):
                if ops[pivot] == '+':
                    max_dp[start][end] = max(max_dp[start][end], max_dp[start][pivot] + max_dp[pivot + 1][end])
                    min_dp[start][end] = min(min_dp[start][end], min_dp[start][pivot] + min_dp[pivot + 1][end])
                else:
                    # 뺼셈의 경우 최댓값='큰값-작은값', 최솟값='작은값-큰값'
                    max_dp[start][end] = max(max_dp[start][end], max_dp[start][pivot] - min_dp[pivot + 1][end])
                    min_dp[start][end] = min(min_dp[start][end], min_dp[start][pivot] - max_dp[pivot + 1][end])

    # 전체 범위의 최댓값
    return max_dp[0][-1]
