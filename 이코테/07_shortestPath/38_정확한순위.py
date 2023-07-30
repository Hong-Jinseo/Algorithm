# 최단경로 (플로이드 워셜)
# 정확한 순위

import sys
input = sys.stdin.readline
INF = int(1e9)

# 학생 수, 비교 횟수
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# graph 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 성적 비교 입력받기
for _ in range(m):
    # 성적: a < b
    x, y = map(int, input().split())
    graph[x][y] = 1

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 둘 중 하나라도 1이면 'graph[a][b] = 1'
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
result = 0
for k in range(1, n+1):
    count = 0
    for others in range(1, n+1):
        if graph[others][k] < INF:
            count += 1
        elif graph[k][others] < INF:
            count += 1

    if count == n:
        result += 1

print(result)
