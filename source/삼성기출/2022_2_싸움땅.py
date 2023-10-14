# 싸움땅 (22년 하반기)
# https://www.codetree.ai/training-field/frequent-problems/problems/battle-ground

import heapq

# 입력 받기
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 총의 공격력

players = []
for _ in range(m):
    x, y, d, p = map(int, input().split())
    players.append([x - 1, y - 1, d, p, graph[x - 1][y - 1]])  # x, y, 방향, 초기 능력치, 총

# 관련 배열 정의
scores = [0] * m
extra = [[[0] for _ in range(n)] for _ in range(n)]  # 한 칸에 2개 이상의 총이 있을 때, 저장 공간

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# NxN을 벗어나는 영역의 좌표를 환산
def change_range(i, now):
    d = players[i][2]

    now = abs(now)
    now %= 2 * (n - 1)

    # 좌표가 여전히 그래프 바깥이면 -> 방향은 상 or 좌
    if now >= n:
        players[i][2] = 0 if (d == 0 or d == 2) else 3
        return 2 * (n - 1) - now

    # 좌표가 그래프 내부라면 -> 방향은 하 or 우
    else:
        players[i][2] = 2 if (d == 0 or d == 2) else 1
        return now


# 범위 체크
def in_range(x):
    return 0 <= x < n


# 플레이어 1칸 움직이기
def move_player(i):
    x, y, direction, _, _ = players[i]

    # 이동 방향에 따른 다음 좌표 찾기
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 맵을 벗어난다면 좌표 변환
    if not in_range(nx):
        nx = change_range(i, nx)
    if not in_range(ny):
        ny = change_range(i, ny)

    # 움직인 좌표 반환
    return (nx, ny)


def find_origin_player(x, y):
    for i, p in enumerate(players):
        if p[0] == x and p[1] == y:
            return i
    return -1


# 남아있는 총이 하나라면
def if_a_gun_left(x, y):
    # extra 중 하나의 값은 0
    if graph[x][y] == -1 and len(extra[x][y]) == 2:
        graph[x][y] = -heapq.heappop(extra[x][y])


# 총 줍기
def get_gun(i):
    x, y, _, _, gun = players[i]

    # 바닥에 놓인 총이 더 강하다면
    if gun < graph[x][y]:
        players[i][-1], graph[x][y] = graph[x][y], players[i][-1]
        return

    # 바닥에 놓인 총이 여러개라면
    elif graph[x][y] < 0:
        new = -extra[x][y][0]
        # 총 변경
        if gun < new:
            players[i][-1] = -heapq.heappop(extra[x][y])
            heapq.heappush(extra[x][y], -gun)

    if_a_gun_left(x, y)


# 진 플레이어 이동
def move_lose_player(i):
    x, y, d, _, _ = players[i]

    for _ in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 앞이 막혔거나 or 사람이 있으면
        if not in_range(nx) or not in_range(ny) or find_origin_player(nx, ny) != -1:
            # 방향 전환
            d = (d + 1) % 4
            continue

            # 방향 갱신 & 해당 방향으로 움직이기
        players[i][2] = d
        mx, my = move_player(i)
        players[i][0], players[i][1] = mx, my

        return


# 패배했을 경우
def lose(i):
    x, y, d, power, gun = players[i]

    # 총 내려놓기
    players[i][-1] = 0

    # 내려놓은 총 관련
    if graph[x][y] == 0:  # 바닥에 총이 없다면
        graph[x][y] = gun
    elif graph[x][y] > 0:  # 총이 1개 있다면
        heapq.heappush(extra[x][y], -graph[x][y])
        heapq.heappush(extra[x][y], -gun)
        graph[x][y] = -1
    else:  # 총이 이미 여러개라면
        heapq.heappush(extra[x][y], -gun)

    # 사람 없는 칸으로 움직이기
    move_lose_player(i)

    # 새로 이동한 곳에 총이 있다면 줍기
    get_gun(i)


# 승리했을 경우
def win(i, lose):
    # 더 강한 공격력의 총으로 변경
    get_gun(i)


# 게임 결과
def result(winner, loser):
    # 점수 계산
    a = players[winner][3] + players[winner][4]
    b = players[loser][3] + players[loser][4]
    scores[winner] += abs(a - b)

    # 이동 & 총 변경
    lose(loser)
    win(winner, loser)


# 게임 라운드 시작
def play():

    for i in range(len(players)):
        # 플레이어가 움직일 칸
        mx, my = move_player(i)

        # 해당 칸에 이미 있는 플레이어 체크
        origin_idx = find_origin_player(mx, my)

        # 플레이어 이동
        players[i][0], players[i][1] = mx, my

        # 이동할 칸에 플레이어가 없다면
        if origin_idx == -1:
            # 총 변경
            get_gun(i)
            continue

        # 이동한 칸에 플레이어가 있다면 -> 싸움
        origin = players[origin_idx]

        # 공격력 기록
        o_power = origin[3] + origin[4]
        m_power = players[i][3] + players[i][4]

        # 원래 있던 플레이어가 더 강하다면
        if o_power > m_power:
            result(origin_idx, i)

        # 새롭게 온 플레이어가 더 강하다면
        elif o_power < m_power:
            result(i, origin_idx)

        # 원래 있던 플레이어의 초기 공격력이 더 강하다면
        elif origin[3] > players[i][3]:
            result(origin_idx, i)

        else:
            result(i, origin_idx)


for _ in range(k):
    play()

    # print('그래프')
    # for g in graph:
    #     print(g)
    # print()

    # print('플레이어')
    # for p in players:
    #     print(p)
    # print()

    # print('총 상태')
    # for e in extra:
    #     print(e)
    # print()

    # print('점수')
    # print(scores)
    # print()
    # print()

print(' '.join(map(str, scores)))