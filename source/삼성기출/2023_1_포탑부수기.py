# 포탑 부수기
# https://www.codetree.ai/training-field/frequent-problems/problems/destroy-the-turret/

from collections import deque
import sys

input = sys.stdin.readline


# 포탄 공격
def shell_attack(attacker, target, joined):
    ax, ay = attacker
    tx, xy = target

    # 공격
    graph[tx][ty] = max(0, graph[tx][ty] - power)

    # 주변 공격
    for dx, dy in direction8:
        nx = (tx + dx) % N
        ny = (ty + dy) % M

        # 공격자라면
        if nx == ax and ny == ay:
            continue

        graph[nx][ny] = max(0, graph[nx][ny] - half_power)
        joined[nx][ny] = True


# 레이저 공격
def laser_attack(attacker, target, joined):
    ax, ay = attacker
    tx, ty = target

    q = deque([(ax, ay, [])])  # 시작 x좌표, 시작 y좌표, 경로 리스트

    visited = [[False] * M for _ in range(N)]
    visited[ax][ay] = True

    # BFS
    while q:
        x, y, route = q.popleft()

        for dx, dy in direction4:
            nx = (x + dx) % N
            ny = (y + dy) % M

            # 이미 방문했거나, 포탑이 무너졌다면
            if visited[nx][ny] or graph[nx][ny] == 0:
                continue

            # 타겟에 도착했다면
            if nx == tx and ny == ty:
                # 타겟 공격
                graph[nx][ny] = max(0, graph[nx][ny] - power)

                # 경로 공격
                for rx, ry in route:
                    graph[rx][ry] = max(0, graph[rx][ry] - half_power)
                    joined[rx][ry] = True

                return True

            # 타겟이 아니라면 -> 경로에 추가
            q.append((nx, ny, route + [(nx, ny)]))
            visited[nx][ny] = True

    # 타겟에 갈 수 없는 경우
    return False


# 가장 약한 포탑의 좌표 찾기 -> 공격자
def find_weakest():
    power = int(1e9)
    x, y = -1, -1

    for i in range(N):
        for j in range(M):
            # 무너진 포탑이 아닐 때
            if graph[i][j] != 0:
                # 더 작은 공격력이 나오면 -> 갱신
                if graph[i][j] < power:
                    power = graph[i][j]
                    x, y = i, j

                # 동일한 공격력이 나오면 -> 우선순위 비교
                elif graph[i][j] == power:
                    # 가장 최근에 공격한 포탑
                    if time[i][j] < time[x][y]:
                        continue
                    elif time[i][j] > time[x][y]:
                        x, y = i, j
                        continue

                    # 공격 시점이 동일하다면 -> 좌표 합 큰 것
                    if i + j < x + y:
                        continue
                    elif i + j > x + y:
                        x, y = i, j
                        continue

                    # 좌표 합이 동일하다면 -> 열 값 큰 것
                    if j < y:
                        continue
                    else:
                        x, y = i, j

    if x == -1:
        return False

    graph[x][y] += (N + M)
    return (x, y)


# 가장 강한 포탑의 좌표 찾기 -> 타겟
def find_strongest(weak_x, weak_y):
    power = 0
    x, y = -1, -1

    for i in range(N):
        for j in range(M):
            # 무너진 포탑이 아니고 and 공격 포탑이 아니라면
            if graph[i][j] != 0 and (i != weak_x or j != weak_y):
                # 더 큰 공격력이 나오면
                if graph[i][j] > power:
                    power = graph[i][j]
                    x, y = i, j

                # 동일한 공격력이 나오면 -> 우선순위 비교
                elif graph[i][j] == power:
                    # 공격한지 오래된 포탑
                    if time[i][j] < time[x][y]:
                        x, y = i, j
                        continue
                    elif time[i][j] > time[x][y]:
                        continue

                    # 공격 시점이 동일하다면 -> 좌표 합 작은 것
                    if i + j < x + y:
                        x, y = i, j
                        continue
                    elif i + j > x + y:
                        continue

                    # 좌표 합이 동일하다면 -> 열 값 작은 것
                    if j < y:
                        x, y = i, j

    return (x, y)


# 2개 이상의 포탑이 남았는지 체크
def if_turret_left():
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                count += 1
    if count == 1:
        return False
    return True


# 입력받기
N, M, K = map(int, input().split())
graph = []  # 공격력
for _ in range(N):
    graph.append(list(map(int, input().split())))

time = [[0] * M for _ in range(N)]  # 공격 시간
direction4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (우하좌상)
direction8 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
power, half_power = 0, 0

# K번 턴 반복
for turn in range(1, K + 1):

    if not if_turret_left():
        break

    joined = [[False] * M for _ in range(N)]

    ## 1. 공격자 선정 ##

    # 가장 약한 포탑 (공격자)
    attacker = find_weakest()
    ax, ay = attacker

    # 가장 강한 포탑 (타겟)
    target = find_strongest(ax, ay)
    tx, ty = target

    # 최종 공격 시간 갱신
    time[ax][ay] = turn

    # 참여 여부 갱신
    joined[ax][ay] = True
    joined[tx][ty] = True

    # 공격력
    power = graph[ax][ay]
    half_power = power // 2

    # print("공격:", attacker, "타겟:", target, '공격력:', power)

    ## 2. 공격자 공격 ##
    # (1) 레이저 공격
    if not laser_attack(attacker, target, joined):
        # (2) 포탄 공격
        shell_attack(attacker, target, joined)

    # 4. 포탑 정비
    for i in range(N):
        for j in range(M):
            if not joined[i][j] and graph[i][j] > 0:
                graph[i][j] += 1

# 남아있는 포탑 중 가장 강한 포탑의 공격력
answer = 0
for row in graph:
    answer = max(answer, max(row))
print(answer)
