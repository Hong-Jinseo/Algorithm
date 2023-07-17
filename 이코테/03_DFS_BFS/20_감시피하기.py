# DFS
# 감시 피하기

n = int(input())
graph, teacher = [], []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 'NO'


# 학생을 발견하면 True, 발견 못하면 False 반환
def detect(x, y, d):
    value = False
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 'S':
            return True
        if graph[nx][ny] == 'O':
            return False
        value = detect(nx, ny, d)
    return value


def dfs(barrier):
    global graph, result

    # 장애물이 이미 3개 설치되었다면
    if barrier == 3:
        # 선생님이 감시 가능한 공간 체크
        for a, b in teacher:
            for direction in range(4):
                # 만약 학생을 찾으면 바로 return (result 값은 'NO')
                if detect(a, b, direction):
                    return
        # 학생을 찾지 못하면 result 값을 'YES'로 수정 후 return
        result = 'YES'
        return

    # 장애물을 3개가 될 때까지 설치 (모든 경우의 수)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                # 벽 세우고 다시 bfs
                graph[i][j] = 'O'
                barrier += 1
                dfs(barrier)

                # 그래프 원상복구
                graph[i][j] = 'X'
                barrier -= 1


dfs(0)
print(result)
