# 최단경로 (다익스트라)
# 숨바꼭질

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for near in graph[now]:
            temp = dist + 1     # 임시 최단거리 = 여기까지의 거리 + 거리 1
            if temp < distance[near]:
                distance[near] = temp
                heapq.heappush(q, (temp, near)) # (업데이트한 최단거리, 헛간 번호)


n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

# 연결된 노드 데이터 삽입
for _ in range(m):
    a, b = map(int, input().split())
    # 가중치는 모두 1로 동일, 따라서 비용은 입력하지 않음
    graph[a].append(b)
    graph[b].append(a)

# 다익스트라
dijkstra(1)

index, max_value = 0, 0
for i in range(1, n+1):
    if distance[i] != INF:
        if max_value < distance[i]:
            max_value = distance[i]
            index = i

count = 0
for i in distance:
    if i == max_value:
        count += 1

print(index, max_value, count)
