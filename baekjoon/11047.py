# 그리디
# 동전 0

n, k = map(int, input().split())
cnt = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

for i in range(n-1, -1, -1):
    cnt += k // coins[i]
    k %= coins[i]

    if k == 0:
        break

print(cnt)
