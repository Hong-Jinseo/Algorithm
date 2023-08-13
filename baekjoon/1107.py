# 브루트 포스
# 리모컨

MAX = 1000000

n = int(input())
m = int(input())
if m > 0:
    lst = list(map(int, input().split()))
else:
    lst = []

count = abs(100 - n)

for k in range(MAX+1):
    num = str(k)        # 입력하려는 채널 (num, k)

    for i in range(len(num)):
        # 입력하려는 채널에 고장난 번호가 포함된다면
        if int(num[i]) in lst:
            break
        # 고장난 번호 없이, 마지막 자리까지 왔다면
        elif i == len(num) - 1:
            # min(기존 최솟값, +/-로 이동해야 하는 횟수 + 버튼 클릭 횟수)
            count = min(count, abs(n-k) + len(num))

print(count)
