# BFS
# 게임 맵 최단거리

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 우 좌 하 상
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    q = deque([(0, 0, 1)])  # x, y, 움직인 횟수

    while q:
        x, y, move = q.popleft()

        if x == n - 1 and y == m - 1:
            return move

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, move + 1))

    return -1
