# 그래프 이론 (크루스칼)
# 도시 분할 계획

import sys
input = sys.stdin.readline


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, x, y):
    x = find_parent(p, x)
    y = find_parent(p, y)

    if x < y:
        p[y] = x
    else:
        p[x] = y


n, m = map(int, input().split())
edges = []   # 간선 정보
result, last = 0, 0  # 유지비 합

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost  # cost 누적
        last = cost     # 마지막 cost (최댓값)

print(result - last)
