# DP
# 가장 긴 증가하는 부분 수열 4

n = int(input())
a = list(map(int, input().split()))

# LIS의 최대 길이 찾기
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# LIS에 해당하는 배열 찾기
idx = max(dp)
answer = []

for i in range(n-1, -1, -1):
    if dp[i] == idx:
        answer.append(a[i])
        idx -= 1

answer.sort()

print(max(dp))
print(' '.join(map(str, answer)))
