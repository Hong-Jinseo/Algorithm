# 메이즈 러너
# https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner

import sys
input = sys.stdin.readline


# 회전한 정사각형을 전체 그래프에 삽입
def insert_square(old, new, x, y):
    n = len(new)

    for i in range(n):
        for j in range(n):
            if new[i][j] > 0:
                new[i][j] -= 1

            old[x + i][y + j] = new[i][j]


# 정사각형을 시계방향으로 회전 후 반환
def rotate_90_degree(square):
    n = len(square)
    new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[j][n - i - 1] = square[i][j]

    return new


# 출구 좌표 찾기
def find_exit(graph):
    n = len(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                return [i, j]


# 회전할 최소 정사각형의 인덱스 찾기
def minimum_square(graph, player):
    ex, ey = find_exit(graph)
    MAX = int(1e9)
    candidate = []

    # 가장 작은 정사각형을 만들 수 있는 플레이어 선별
    for px, py in player:
        # 해당 플레이어를 포함할 때 만들어지는 정사각형의 변의 길이
        length = max(abs(ex - px), abs(ey - py)) + 1

        # 변의 길이가 같은 케이스가 이미 존재한다면 -> 추가
        if length == MAX:
            candidate.append([length, px, py])

        # 해당 변의 길이가 최소라면 -> 초기화
        elif length < MAX:
            MAX = length
            candidate = [[length, px, py]]

    # 선별된 플레이어 중, 가장 좌측 상단의 좌표를 갖는 값 찾기
    final = []
    for length, px, py in candidate:
        # 최소 사각형의 모서리 찾기
        x1, y1 = min(px, ex), min(py, ey)  # 왼쪽 위
        x2, y2 = max(px, ex), max(py, ey)  # 오른쪽 아래

        # x, y좌표 각각 얼마만큼의 여유 공간이 있는지 파악
        more_x = length - (x2 - x1 + 1)
        more_y = length - (y2 - y1 + 1)

        # 0보다 큰 수 중, 여유공간만큼 왼쪽 상단으로 이동한 좌표
        final.append([max(0, x1 - more_x), max(0, y1 - more_y), length])

    # X 오름차순, Y 오름차순
    final.sort()
    return final[0]


# 참가자 이동
def move_player(graph, player):
    g = len(graph)
    exit = find_exit(graph)

    # 상하좌우 (좌우 이동보다 상하 이동이 우선된다)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 출구로부터 플레이어까지의 거리 차
    origin = abs(exit[0] - player[0]) + abs(exit[1] - player[1])

    # 출구에 도착한 상태라면
    if origin == 0:
        # [출구 도착여부, 현재 x좌표, 현재 y좌표, 이동 횟수]
        return [True, exit[0], exit[1], 0]

    # 출구와 가장 가까워지는 좌표 찾기
    for i in range(4):
        nx = player[0] + dx[i]
        ny = player[1] + dy[i]

        if 0 <= nx < g and 0 <= ny < g:
            # 출구와 가까워지는 방향일 때
            if abs(exit[0] - nx) + abs(exit[1] - ny) < origin:
                # 출구에 도착했다면
                if graph[nx][ny] == -1:
                    return [True, nx, ny, 1]

                # 이동 가능하다면 (벽이 아니라면)
                elif graph[nx][ny] == 0:
                    return [False, nx, ny, 1]

    # 이동하지 못한 경우
    return [False, player[0], player[1], 0]


N, M, K = map(int, input().split())  # 미로의 크기, 참가자 수, 시간초
answer = 0

# 미로 입력받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 참가자 좌표 입력받기
player = []
for _ in range(M):
    x, y = map(int, input().split())
    player.append([x - 1, y - 1])  # 현재 x좌표, 현재 y좌표

# 출구 좌표 입력받기
ex, ey = list(map(int, input().split()))
exit = [ex - 1, ey - 1]
graph[exit[0]][exit[1]] = -1

# 게임 시작
for _ in range(1, K + 1):
    # 모든 플레이어가 탈출했다면
    if not player:
        break


    ## 참가자 이동 ##
    moved = []
    for p in player:
        tempp = move_player(graph, p)
        answer += tempp[-1]     # 이동 거리 업데이트

        # 아직 출구에 도달하지 못했다면
        if not tempp[0]:
            moved.append([tempp[1], tempp[2]])


    # 모든 플레이어가 탈출했다면
    if not moved:
        break

    ## 미로 회전 ##
    mx, my, mlength = minimum_square(graph, moved)

    # 회전할 사각형 분리
    square_to_rotate = [[0] * mlength for _ in range(mlength)]
    truned = []
    for i in range(mlength):
        for j in range(mlength):
            square_to_rotate[i][j] = graph[mx + i][my + j]

            # 분리될 사각형에 있는 참가자를 회전
            while [mx + i, my + j] in moved:
                moved.remove([mx + i, my + j])
                truned.append([mx + j, my + mlength - i - 1])

    # 사용자 좌표 갱신
    player = moved + truned

    # 사각형 회전, 기존 미로에 삽입
    rotated = rotate_90_degree(square_to_rotate)
    insert_square(graph, rotated, mx, my)


# 최종 좌표 찾기
exit = find_exit(graph)

print(answer)
print(exit[0] + 1, exit[1] + 1)
