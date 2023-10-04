# BFS
# 게임 맵 최단거리

from collections import deque


def solution(maps):
    n = len(maps)  # x
    m = len(maps[0])  # y

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[False] * m for _ in range(n)]

    q = deque([(0, 0, 1)])  # (x좌표, y좌표, 움직인 횟수)
    visited[0][0] = True

    while q:
        x, y, move = q.popleft()

        if x == n - 1 and y == m - 1:
            return move

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] == 1:  # 벽이 없으면
                    q.append((nx, ny, move + 1))
                    visited[nx][ny] = True

    return -1