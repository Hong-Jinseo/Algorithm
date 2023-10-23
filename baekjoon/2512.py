# 이분탐색
# 예산

n = int(input())
plans = list(map(int, input().split()))
m = int(input())
start, end = 0, max(plans)

# 이분 탐색
while start <= end:
    mid = (start+end) // 2
    total = 0               # 총 지출

    for i in plans:
        total += mid if i > mid else i

    # 지출 <= 예산
    if total <= m:
        start = mid+1
    # 지출 > 예산
    else:
        end = mid-1

print(end)
