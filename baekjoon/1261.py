# BFS
# 알고스팟

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().strip())))

q = deque([(0, 0)])  # (x, y, cnt)

# 해당 위치에 도달할때까지 부순 벽의 개수 (-1이면 방문 0회)
count = [[-1] * n for _ in range(m)]
count[0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y = q.popleft()

    if x == m-1 and y == n-1:
        print(count[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            # 벽이 없다면
            if graph[nx][ny] == 0 and (count[nx][ny] == -1 or count[nx][ny] > count[x][y]):
                count[nx][ny] = count[x][y]
                q.appendleft((nx, ny))
            # 벽이 있다면
            elif graph[nx][ny] == 1 and (count[nx][ny] == -1 or count[nx][ny] > count[x][y] + 1):
                count[nx][ny] = count[x][y] + 1
                q.append((nx, ny))
