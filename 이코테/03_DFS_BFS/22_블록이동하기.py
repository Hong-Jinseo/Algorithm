# bfs
# 블록 이동하기

from collections import deque


def solution(board):
    n = len(board)

    # 하 우 상 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 로봇 x좌표, 로봇 y좌표, 방향(가로0, 세로1), 이동 시간
    queue = deque([(0, 0, True, 0)])
    visited = {(0, 0, True)}

    while queue:
        x1, y1, d, t = queue.popleft()
        # 가로/세로 방향에 맞게 로봇의 두번째 부분 위치 조정
        x2, y2 = x1 + dx[d], y1 + dy[d]

        if x2 == n-1 and y2 == n-1:
            return t

        # 상하좌우
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]

            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                # 이미 방문했거나, 벽인 경우
                if (nx1, ny1, d) in visited or board[nx1][ny1] == 1 or board[nx2][ny2] == 1:
                    continue

                # 방향 유지한 채 이동
                queue.append((nx1, ny1, d, t+1))
                visited.add((nx1, ny1, d))

                # 방향 회전 # 하 우 상 좌
                # 가로일 때 아래, 세로일 때 오른쪽이 벽이 아니라면
                if (d==0 and i==1) or (d==1 and i==0):
                    if (x1, y1, not d) not in visited:
                        queue.append((x1, y1, not d, t+1))
                        visited.add((x1, y1, not d))
                    if (x2, y2, not d) not in visited:
                        queue.append((x2, y2, not d, t+1))
                        visited.add((x2, y2, not d))
                # 가로일 때 위, 세로일 때 왼쪽이 벽이 아니라면
                if (d==0 and i==3) or (d==1 and i==2):
                    if (nx1, ny1, not d) not in visited:
                        queue.append((nx1, ny1, not d, t+1))
                        visited.add((nx1, ny1, not d))
                    if (nx2, ny2, not d) not in visited:
                        queue.append((nx2, ny2, not d, t+1))
                        visited.add((nx2, ny2, not d))

    return -1


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	))
