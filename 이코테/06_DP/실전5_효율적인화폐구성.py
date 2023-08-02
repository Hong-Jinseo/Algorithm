# DP
# 효율적인 화폐 구성

# 화폐 종류, 목표치
n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

# 화폐 종류만큼 반복
for i in range(n):
    for j in range(coins[i], m+1):
        # d[j]보다 코인 한 개가 모자랄 때, 해당 값을 만들 수 있다면(10001이 아니라면)
        if d[j-coins[i]] != 10001:
            # min(d[j]에 저장된 값, d[j-coins[i]]에 coins[i] 코인 한개를 더한 값)
            d[j] = min(d[j], d[j-coins[i]] + 1)

print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
