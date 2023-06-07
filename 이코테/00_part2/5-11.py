# BFS (최적의 경로)
# 미로 탈출

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우 (좌표평면 아닌 이차배열 기준)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 미로를 벗어나면 무시

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물을 만나면 무시
            if graph[nx][ny] == 0:
                continue

            # 방문 안 한 노드라면
            if graph[nx][ny] == 1:
                #
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0, 0))
