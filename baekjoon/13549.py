# BFS
# 숨바꼭질 3

from collections import deque
MAX = 100000

n, k = map(int, input().split())
q = deque([(n, 0)])     # (현위치, 시간)

visited = [False] * (MAX+1)
visited[n] = True

while q:
    now, sec = q.popleft()

    if now == k:
        print(sec)
        break

    for i in ((now - 1, sec + 1, False), (2 * now, sec, True), (now + 1, sec + 1, False)):
        now2, sec2, priority = i

        if 0 <= now2 <= MAX and not visited[now2]:
            if priority:
                q.appendleft((now2, sec2))
            else:
                q.append((now2, sec2))
            visited[now2] = True
