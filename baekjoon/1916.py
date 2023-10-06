# 다익스트라
# 최소비용 구하기

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

# 입력받기
n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c]) # s에서 e로 가는데 c의 비용
start, end = map(int, input().split())

# 거리 그래프
distance = [INF] * (n+1)
distance[start] = 0

# 우선순위큐
queue = []
heapq.heappush(queue, (distance[start], start))  # 비용, 위치

# 다익스트라
while queue:
    cost, node = heapq.heappop(queue)
    
    # 목적지에 도착했다면 -> 
    if node == end:
        print(distance[node])
        break
    
    # 이미 처리한 노드라면 -> pass
    if distance[node] < cost:
        continue
    
    # 현재 노드에서 갈 수 있는 다른 노드들 조회
    for new_node, new_cost in graph[node]:
        # 현재 노드를 거쳐 새로운 노드에 가기 < 이미 저장된 값
        if cost + new_cost < distance[new_node]:
            distance[new_node] = cost + new_cost
            heapq.heappush(queue, (distance[new_node], new_node))

