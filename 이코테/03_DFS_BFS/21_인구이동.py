# DFS
# 인구 이동

# python의 최대 재귀 깊이를 1,000,000으로 변경
import sys
sys.setrecursionlimit(10**6)

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0
visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


# 함수 : 특정 국가를 기준으로 연합을 반환
def make_union(x, y, union):
    global flag
    union.add((x, y))       # 연합 집합에 추가
    visited[x][y] = True    # 방문 기록

    # DFS
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 오늘 방문하지 않았고 + 인구수의 차가 l과 r 사이인 인근 국가 [nx][ny]
            if not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    flag = True
                    union = make_union(nx, ny, union)       # 인근 국가를 통해 연합 확장
    return union


# 함수 : 특정 연합의 인구를 이동
def calculate(union):
    global graph
    total = 0
    for x, y in union:
        total += graph[x][y]
    count = int(total / len(union))
    for x, y in union:
        graph[x][y] = count


flag = False    # 인구 이동 여부를 기록

while True:
    # 하루동안 진행되는 인구 이동
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                st = set()      # 국가[i][j]와 연합인 국가들을 기록하는 집합
                st = make_union(i, j, st)
                calculate(st)

    # 인구 이동이 없으면
    if not flag:
        break
    # 인구 이동이 있으면
    else:
        result += 1
        flag = False
        visited = [[False] * n for _ in range(n)]

print(result)
