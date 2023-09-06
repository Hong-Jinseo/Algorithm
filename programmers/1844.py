# BFS
# 게임 맵 최단거리

from collections import deque


def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    n = len(maps)
    m = len(maps[0])

    q = deque([(0, 0, 1)])  # (x, y, move)
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y, move = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 다음 노드가 상대 진영이면
                if nx == n - 1 and ny == m - 1:
                    return move + 1

                # 다음 노드가 1이면
                elif maps[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny, move + 1))  # 방문 예정 목록에 추가
                    visited[nx][ny] = True  # 방문 기록
    return -1
