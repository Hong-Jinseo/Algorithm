# 최단거리 (플로이드 워셜)
# 플로이드

import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())    # 도시의 개수 (정점)
m = int(input())    # 버스의 개수 (간선)

# 최단거리 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    graph[i][i] = 0

# 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for gh in graph[1:]:
    for g in gh[1:]:
        if g == INF:
            print(0, end=' ')
        else:
            print(g, end=' ')
    print()