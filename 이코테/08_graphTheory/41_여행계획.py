# 그래프 이론
# 여행 계획

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
parent = [i for i in range(n+1)]

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            union_parent(parent, i+1, j+1)

cities = list(map(int, input().split()))


result = "YES"

# 내 풀이
first = find_parent(parent, cities[0])
for city in cities:
    if first != find_parent(parent, city):
        result = "NO"
        break

# 교재 풀이
# for i in range(m-1):
#     if find_parent(parent, cities[i]) != find_parent(parent, cities[i+1]):
#         result = "NO"
#         break

print(result)
