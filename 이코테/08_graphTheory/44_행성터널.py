# 그래프 이론 (최소 스패닝 트리, 크루스칼)
# 행성 터널

import copy
import sys
input = sys.stdin.readline


def find_parent(p, a):
    if p[a] != a:
        p[a] = find_parent(p, p[a])
    return p[a]


def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


graph = []
edges = []

n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    graph.append((i, x, y, z))

x_list = copy.deepcopy(graph)
y_list = copy.deepcopy(graph)
z_list = copy.deepcopy(graph)

x_list.sort(key=lambda v: v[1])
y_list.sort(key=lambda v: v[2])
z_list.sort(key=lambda v: v[3])

for i in range(n-1):
    # (cost, a행성, b행성)
    edges.append((abs(x_list[i][1] - x_list[i+1][1]), x_list[i][0], x_list[i+1][0]))
    edges.append((abs(y_list[i][2] - y_list[i+1][2]), y_list[i][0], y_list[i+1][0]))
    edges.append((abs(z_list[i][3] - z_list[i+1][3]), z_list[i][0], z_list[i+1][0]))

edges.sort()
parent = [i for i in range(len(edges))]
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
