# BFS
# 숨바꼭질

from collections import deque
MAX = 100000

n, k = map(int, input().split())
visited = [False] * (MAX+1)

q = deque([(n, 0)])
visited[n] = True
cnt = 0

while q:
    now, cnt = q.popleft()
    if now == k:
        print(cnt)
        break

    for next_ in (now-1, now+1, 2*now):
        if 0 <= next_ <= MAX and not visited[next_]:
            q.append((next_, cnt+1))
            visited[next_] = True
