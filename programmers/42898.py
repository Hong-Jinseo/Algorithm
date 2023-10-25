# DP
# 등굣길

# 2차 풀이
def solution(m, n, puddles):
    dp = [[0] * (m + 2) for _ in range(n + 2)]
    dp[1][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 웅덩이라면
            if [j, i] in puddles:  # 주의!! 행, 열 반대로 주어짐
                dp[i][j] = 0
                continue

            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]
