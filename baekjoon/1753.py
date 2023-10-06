# 다익스트라 (그리디)
# 최단경로

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (v+1)
distance[k] = 0

heap = []
heapq.heappush(heap, (distance[k], k))  # k까지의 거리

while heap:
    cost, node = heapq.heappop(heap)
    # 이미 기록된 비용이 최소라면
    if distance[node] < cost:
        continue

    for new_node, new_cost in graph[node]:
        costs = cost + new_cost
        if costs < distance[new_node]:
            distance[new_node] = costs
            heapq.heappush(heap, (costs, new_node))

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)
