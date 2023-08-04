# 그래프 이론 (union)
# 팀 결성

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
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
result = []

for i in range(m):
    op, a, b = map(int, input().split())

    # 합치기 연산
    if op == 0:
        union_parent(parent, a, b)
    # 같은 팀 여부 확인 연산
    else:
        if parent[a] == parent[b]:
            result.append('YES')
        else:
            result.append('NO')

print('\n'.join(result))
