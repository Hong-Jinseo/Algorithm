# 감시
# DFS

import copy

# 입력받기
n, m = map(int, input().split())
graph = []  # 전체 좌표
cctv = []  # cctv의 (종류, x, y)

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j, value in enumerate(temp):
        if value in [1, 2, 3, 4, 5]:
            cctv.append((value, i, j))


# 각 cctv가 바라볼 수 있는 방향 (dxdy 기준)
mode = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]]
}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def fill(arr, direct, x, y):
    for d in direct:
        nx, ny = x, y

        while True:
            nx += dx[d]
            ny += dy[d]

            # 범위를 벗어나면
            if not (0 <= nx < n and 0 <= ny < m):
                break

            # 벽을 만나면
            if arr[nx][ny] == 6:
                break

            # 빈 공간이면 -> 감시의 표시로 7 기입
            elif arr[nx][ny] == 0:
                arr[nx][ny] = 7


def dfs(array, num):
    global min_value

    # 모든 cctv를 탐색했다면
    if num == len(cctv):
        # 빈 공간 세기
        cnt = 0
        for row in array:
            cnt += row.count(0)
        min_value = min(cnt, min_value)
        return

    #
    new_array = copy.deepcopy(array)
    cctv_type, x, y = cctv[num]

    for direct in mode[cctv_type]:
        # 배열 칠하기
        fill(new_array, direct, x, y)
        # 칠한 배열로 dfs 돌리기
        dfs(new_array, num + 1)
        # 칠했던 배열을 전 상태로 초기화
        new_array = copy.deepcopy(array)


min_value = int(1e9)
dfs(graph, 0)
print(min_value)
