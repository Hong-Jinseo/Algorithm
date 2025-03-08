# DFS/BFS
# DFS와 BFS

from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 전체 저장
    graph[a][b] = True
    graph[b][a] = True

    # 정점만 저장
    graph2[a].append(b)
    graph2[b].append(a)

# ====================================

# 방문기록, true/false
visited_bfs_tf = [False] * (N+1)
visited_dfs_tf = [False] * (N+1)

# BFS, true/false
def bfs_tf(start):
    q = deque([start])  # 시작지점 V
    visited_bfs_tf[start] = True

    while q:
        now = q.popleft()
        print(now, end=" ")
        for next in range(1, N+1):
            # 연결 and 미방문
            if graph[now][next] and not visited_bfs_tf[next]:
                q.append(next)
                visited_bfs_tf[next] = True

def dfs_tf(now):
    visited_dfs_tf[now] = True
    print(now, end=" ")
    for next in range(1, N+1):
        if not visited_dfs_tf[next] and graph[now][next]:
            dfs_tf(next)
            visited_dfs_tf[next] = True

# ====================================

# 방문기록, 정점 저장
visited_bfs_node = [False] * (N+1)
visited_dfs_node = [False] * (N+1)

for g in graph2:
    g.sort()

# BFS, node
def bfs_node(start):
    q = deque([start])
    visited_bfs_node[start] = True

    while q:
        now = q.popleft()
        print(now, end=" ")

        for next in graph2[now]:
            if not visited_bfs_node[next]:
                q.append(next)
                visited_bfs_node[next] = True

def dfs_node(now):
    visited_dfs_node[now] = True
    print(now, end=" ")

    for next in graph2[now]:
        if not visited_dfs_node[next]:    
            dfs_node(next)

# ====================================
print("DFS")
dfs_tf(V)
print()
dfs_node(V)
print()
print()

print("BFS")
bfs_tf(V)
print()
bfs_node(V)
print()