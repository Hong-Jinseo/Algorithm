# 그리디
# 볼링공 고르기

n, m = map(int, input().split())
balls = list(map(int, input().split()))
weight = [0] * (m+1)
total = 0

# 공 무게 카운트
for ball in balls:
    weight[ball] += 1

# for i in range(1, m+1):
#     for j in range(i+1, m+1):
#         total += weight[i] * weight[j]

for i in range(1, m+1):
    n -= weight[i]              # n = n - (A가 선택 가능한 공의 개수) = (B가 선택 가능한 공의 개수)
    total += weight[i] * n      # total += (A가 선택 가능한 공의 개수) * (B가 선택 가능한 공의 개수)

print(total)
