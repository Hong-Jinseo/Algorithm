# 최단경로
# 플로이드

import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 그래프 정보 입력받기
for _ in range(m):
    # 출발도시, 도착도시, 비용
    a, b, c = map(int, input().split())

    # 노선은 여러개 있을 수 있으므로, 최소비용인 노선을 저장한다
    new_c = min(graph[a][b], c)
    graph[a][b] = new_c

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 답 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
