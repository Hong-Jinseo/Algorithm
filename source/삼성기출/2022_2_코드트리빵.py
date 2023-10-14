# 코드트리 빵
# https://www.codetree.ai/training-field/frequent-problems/problems/codetree-mon-bread


from collections import deque
import heapq

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

store = []
for _ in range(m):
    a, b = map(int, input().split())
    store.append([a - 1, b - 1])

INF = int(1e9)
EMPTY = [-1, -1]
people = [EMPTY] * m

# 상 좌 우 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

time = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(sx, sy):
    q = deque([[sx, sy]])
    # route = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] != 2:
                # visited[nx][ny] = True
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited


def simulate(t):
    # 1. 격자 위의 사람들이 편의점을 향해 이동
    for i, person in enumerate(people):
        if person == EMPTY or person == store[i]:
            # print('진서', i, person)
            continue

        # 목적지 편의점 정보
        sx, sy = store[i]
        route = bfs(sx, sy)

        px, py = person

        min_dist, min_x, min_y = INF, -1, -1

        # 최단거리 선택
        for k in range(4):
            nx = px + dx[k]
            ny = py + dy[k]

            if in_range(nx, ny) and route[nx][ny]:
                if route[nx][ny] < min_dist:
                    min_dist = route[nx][ny]
                    min_x, min_y = nx, ny

        # 사람 움직이기
        people[i] = [min_x, min_y]

    # 2. 편의점 도착 & 비활성화
    for i, person in enumerate(people):
        if person == store[i]:
            px, py = person
            graph[px][py] = 2

    # 3. t초에 t번 사람이 가장 가까운 베이스캠프로 이동
    if t < m and people[t] != store[i]:
        # t번 사람이 가려는 편의점 주소
        sx, sy = store[t]

        # 편의점에서 역순으로 bfs 수행
        route = bfs(sx, sy)

        # 목표 편의점과 모든 베이스캠프 사이의 거리 조사
        candidates = []
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1 and route[i][j] != False:
                    heapq.heappush(candidates, (route[i][j], i, j))

        # 가장 가까운 베이스캠프
        _, bx, by = candidates[0]
        people[t] = [bx, by]
        graph[bx][by] = 2


def finish():
    for i in range(m):
        if people[i] != store[i]:
            return False
    return True


# print(store)
# print()
# print('처음', people)

while True:
    time += 1
    simulate(time - 1)
    # print(str(time)+'초', people)
    if finish():
        break

print(time)
