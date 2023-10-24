# 이분탐색
# 랜선 자르기

# k개의 랜선을 n개의 같은 길이의 랜선으로 만들기
k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]

# 만들 수 있는 최대 랜선의 길이

start, end = 1, max(length)

while start <= end:
    mid = (start + end) // 2    # 랜선의 최소 길이
    cnt = 0

    # mid보다 길다면 -> 랜선을 만들 수 있음
    for rope in length:
        if mid <= rope:
            cnt += rope // mid  # K개 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정 -> 0으로 나눌 걱정 X

    # 랜선을 더 만들어야 하면
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(start - 1)
