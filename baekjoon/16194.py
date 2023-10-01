# DP
# 카드 구매하기 2

n = int(input())
cards = [0] + list(map(int, input().split()))

dp = []
for c in cards:
    dp.append(c)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + cards[j])

print(dp[-1])
