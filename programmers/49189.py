# 그래프 (BFS)
# 가장 먼 노드

from collections import deque

INF = int(1e9)


def solution(n, edge):
    graph = [[] for i in range(n + 1)]

    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)

    # BFS
    distance = [INF] * (n + 1)

    q = deque([1])
    distance[1] = 0

    while q:
        now = q.popleft()

        # now에서 도달할 수 있는 노드들
        for node in graph[now]:
            # 아직 처리하지 않은 노드라면
            if distance[node] == INF:
                distance[node] = distance[now] + 1
                q.append(node)

    return distance[1:].count(max(distance[1:]))