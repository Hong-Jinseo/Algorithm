# BFS
# 특정 거리의 도시 찾기

from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 정보
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

# x를 시작점으로 bfs
queue = deque([x])
while queue:
    now = queue.popleft()
    for post in graph[now]:
        # post 노드가 아직 방문하지 않은 노드라면
        if distance[post] == -1:
            distance[post] = distance[now] + 1
            queue.append(post)

none = True
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        none = False

if none:
    print(-1)
