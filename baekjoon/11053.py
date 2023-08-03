# DP
# 가장 긴 증가하는 부분 수열 (LIS)

n = int(input())
a = list(map(int, input().split()))

# i번째 인덱스에서 끝나는 부분 수열의 길이
d = [1] * n

# i가 뒤에 있는 수, j가 앞에 있는 수
for i in range(1, n):
    for j in range(i):
        # 뒤에 있는 수가 더 클 때 (LIS를 만들 수 있을 때)
        # 이미 구성된 LIS의 마지막 값 < 새롭게 추가되는 값
        if a[j] < a[i]:
            d[i] = max(d[i], d[j] + 1)
            # d[j]+1: j번째 인덱스에서 끝나는 LIS의 마지막에 a[i]를 추가했을 때 LIS 길이
            # d[i]: a[i]를 추가하지 않은, 기존 값

print(max(d))
