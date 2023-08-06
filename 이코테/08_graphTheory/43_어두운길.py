# 그래프 이론(크루스칼)
# 어두운 길

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


# input
n, m = map(int, input().split())

roads = []

for i in range(m):
    x, y, z = map(int, input().split())
    roads.append((z, x, y))

roads.sort()

# union-find
parent = [i for i in range(n+1)]

result = 0
for road in roads:
    cost, x, y = road
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
    else:
        result += cost

print(result)
