# 브루트 포스
# 테트로미노

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = -1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]


def search(x, y, index, total):
    global result
    visited[x][y] = True

    if index > 4:
        result = max(result, total)
        return

    total += graph[x][y]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                search(nx, ny, index+1, total)
                visited[nx][ny] = False

    visited[x][y] = False


def searchT(x, y):
    global result
    row, col = 0, 0

    # ㅓ, ㅏ
    if x+2 < n:
        for k in range(3):
            row += graph[x+k][y]
        if y-1 >= 0:
            result = max(result, row + graph[x+1][y-1])
        if y+1 < m:
            result = max(result, row + graph[x+1][y+1])

    # ㅗ, ㅜ
    if y+2 < m:
        for k in range(3):
            col += graph[x][y+k]
        if x-1 >= 0:
            result = max(result, col + graph[x-1][y+1])
        if x+1 < n:
            result = max(result, col + graph[x+1][y+1])


for i in range(n):
    for j in range(m):
        search(i, j, 1, 0)
        searchT(i, j)

# searchT(1, 1)
print(result)
