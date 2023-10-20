# 이분탐색
# 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# m개의 나무를 가져가려고 함

start, end = 0, max(trees) - 1

while start <= end:
    # 나무를 자르는 기준 높이
    h = (start + end) // 2
    total = 0

    for t in trees:
        if h < t:
            total += t - h

    # 나무를 더 잘라야 하면 -> h를 더 낮게 잡음
    if total < m:
        end = h - 1
    # 나무를 덜 잘라야 하면 -> h를 더 높게 잡음
    else:
        start = h + 1

print(start - 1)
