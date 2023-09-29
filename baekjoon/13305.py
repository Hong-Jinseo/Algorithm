# 그리디
# 주유소

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
answer = 0

now_cost = int(1e9)

for i in range(n-1):
    now_cost = min(now_cost, cost[i])
    answer += now_cost * dist[i]

print(answer)
