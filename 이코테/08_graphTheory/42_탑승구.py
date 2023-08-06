# 그래프 이론
# 탑승구

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


g = int(input())    # 탑승구 수
p = int(input())    # 비행기 수
gate = [i for i in range(g+1)]           # i번째 비행기가 도깅 가능한 탑승구 범위

result = 0

for i in range(p):
    num = int(input())  # 1~g 사이 값
    parent = find_parent(gate, num)
    if parent == 0:
        break
    union_parent(gate, parent, parent-1)
    result += 1

print(result)
