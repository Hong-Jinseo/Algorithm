# DP
# 쉬운 계단 수

n = int(input())

# [자릿수][끝나는 수] = 개수
dp = [[0 for _ in range(10)] for i in range(n+1)]
dp[1] = [0] + [1 for _ in range(9)]

for i in range(2, n+1):
    for j in range(1, 9):
        # 마지막 숫자가 1~8인 경우
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

print(sum(dp[n]) % 1000000000)
