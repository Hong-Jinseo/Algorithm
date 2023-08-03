# DP
# 병사 배치하기

n = int(input())
lst = list(map(int, input().split()))

# 남아있는 병사 수
d = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] < lst[j]:
            d[i] = max(d[i], d[j]+1)

print(n - max(d))




