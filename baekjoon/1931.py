# 그리디
# 회의실 배정

n = int(input())
time = []
for i in range(n):
    s, e = map(int, input().split())
    time.append((e, s))

time.sort()

now, cnt = 0, 0
for e, s in time:
    if s >= now:
        now = e
        cnt += 1

print(cnt)

