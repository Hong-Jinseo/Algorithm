# DP
# 오르막 수

n = int(input())
dp = [1] * 10

# n이 1인 경우 제외 (dp값이 1이기 때문에 갱신할 필요 X)
for _ in range(n-1):
    # dp[0]은 이미 1이기 때문에 갱신할 필요 X
    for i in range(1, 10):
        dp[i] += dp[i-1]

print(sum(dp) % 10007)
