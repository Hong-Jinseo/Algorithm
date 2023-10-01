# DP
# 이친수

n = int(input())

# dp[자리수][끝나는 숫자] = 개수
dp = [[0, 0] for i in range(n+1)]
dp[1] = [0, 1]  # 1

for i in range(2, n+1):
    # 0으로 끝나는 건 = 앞자리가 0 혹은 1일 때 가능
    dp[i][0] = dp[i-1][0] + dp[i-1][1]

    # 1로 끝나는 건 = 앞자리가 0일 때에만 가능
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))

