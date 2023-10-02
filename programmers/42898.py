# DP
# 등굣길

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][0] = 1
    # 시작점 dp[1][1]을 1로 만들기 위함
    # (dp[1][1] = dp[1][0] + dp[0][1] = 1 + 0)

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            # 만약 (x, y)가 웅덩이면 -> 값을 0으로
            if [y, x] in puddles:
                dp[x][y] = 0
                continue

            # (x, y)에 가는 경우의 수 = 위 + 왼쪽
            dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % 1000000007

    return dp[-1][-1]
