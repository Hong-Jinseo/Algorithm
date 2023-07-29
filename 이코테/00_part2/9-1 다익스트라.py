# 최단 경로
# 간단한 다익스트라 알고리즘 소스코드

import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한 (10억)

# 노드 수, 간선 수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
# 그래프 정보
graph = [[] for _ in range(n + 1)]
# 방문 여부 체크
visited = [False] * (n + 1)
# 최단 거리 테이블 (무한으로 초기화)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # a 노드에서 b 노드로 가는 비용이 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

''' input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

''' output
0
2
3
1
2
4
'''
