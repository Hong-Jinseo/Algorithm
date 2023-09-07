# BFS
# 아이템 줍기

from collections import deque


# 전체의 테두리인지 확인
def check_line(rect, a, b):
    # 내부
    for r in rect:
        x1, y1, x2, y2 = r
        if x1 < a < x2 and y1 < b < y2:
            return False

    # 내부 아닌 테두리
    for r in rect:
        x1, y1, x2, y2 = r
        if x1 <= a <= x2:
            if b == y1 or b == y2:
                return True

        if y1 <= b <= y2:
            if a == x1 or a == x2:
                return True

    # 외부
    return False


def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 값을 2배 늘리기
    MAX = 102
    for i in range(len(rectangle)):
        for j in range(4):
            rectangle[i][j] *= 2

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    # 상하좌우 좌표
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque([(characterX, characterY, 0)])
    visited = [[False] * MAX for _ in range(MAX)]
    visited[characterX][characterY] = True

    while q:
        x, y, move = q.popleft()

        if x == itemX and y == itemY:
            return move // 2  # 결과값/2를 반환

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if check_line(rectangle, nx, ny) and not visited[nx][ny]:
                q.append((nx, ny, move + 1))
                visited[nx][ny] = True

    return -1


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
# 17
