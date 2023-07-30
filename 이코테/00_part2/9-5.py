# 최단 경로
# 전보

import heapq
INF = int(1e9)

# 도시 수, 통로 수, 메세지를 보내고자 하는 도시
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    # x에서 y로 이어지는 통로, 소요시간 z
    x, y, z = map(int, input().split())
    graph[x].append((z, y))         # (소요시간, 도시명)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # (소요시간, 도시명)
    distance[start] = 0

    while q:
        dist, city = heapq.heappop(q)
        if distance[city] < dist:
            continue

        # city의 인접 도시 정보(거리, 도시명)
        for i in graph[city]:
            cost = dist + i[0]  # city를 거쳐서 i에 가는 비용
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


dijkstra(c)
count, maximum = 0, 0

for d in distance:
    if d != INF:
        count += 1
        maximum = max(maximum, d)

# count에서 자기자신 하나 제외
print(count-1, maximum)
