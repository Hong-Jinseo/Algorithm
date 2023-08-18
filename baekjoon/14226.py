# BFS
# 이모티콘

from collections import deque

s = int(input())
q = deque([(1, 0, 0)])     # 만들어진 이모티콘, 시간

visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True

while q:
    now, copy, sec = q.popleft()

    if now == s:
        print(sec)
        break

    for i in ((now, now), (now+copy, copy), (now-1, copy)):
        now2, copy2 = i
        if 0 < now2 <= 1000 and 0 < copy2 <= 1000:
            if not visited[now2][copy2]:
                q.append((now2, copy2, sec+1))
                visited[now2][copy2] = True
