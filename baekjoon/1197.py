# 크루스칼
# 최소 스패닝 트리

import sys
input = sys.stdin.readline


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b


v, e = map(int, input().split())

graph = []
for _ in range(e):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))
graph.sort()

parent = [i for i in range(v+1)]
answer = 0

for cost, s, e in graph:
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        answer += cost

print(answer)
