# 최단경로 (다익스트라)
# 화성 탐사

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for z in range(t):
    n = int(input())

    graph = []                              # 그래프 정보
    cost = [[INF] * n for _ in range(n)]    # 최소비용

    # 데이터 입력받기 (각 칸을 지나기 위한 비용)
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 다익스트라
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))  # (비용, x, y)
    cost[0][0] = graph[0][0]

    while q:
        c, x, y = heapq.heappop(q)
        if cost[x][y] < c:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                accumulate = c + graph[nx][ny]  # 누적값
                if accumulate < cost[nx][ny]:
                    cost[nx][ny] = accumulate
                    heapq.heappush(q, (accumulate, nx, ny))

    result.append(cost[n-1][n-1])

for data in result:
    print(data)
