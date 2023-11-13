# DP
# 타일 채우기

n = int(input())

if n % 2 != 0:
    print(0)
    exit()

dp = [0] * (n+1)
dp[2] = 3

for i in range(4, n+1, 2):
    # 2개 전 공간 * 가로가 2인 공간에 들어갈 수 있는 경우의 수 3개 + 가로가 4인 공간에만 들어갈 수 있는 모양 2개
    dp[i] = dp[i-2] * 3 + 2

    # 가로가 4인 공간에만 들어갈 수 있는 모양 2개
    for j in range(2, i-2, 2):
        dp[i] += dp[j] * 2

print(dp[n])
