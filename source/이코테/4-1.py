# 구현
# 상하좌우

n = int(input())
plan = list(input().split())

# L왼, R오, U위, D아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

x, y = 0, 0

for data in plan:
    i = types.index(data)
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n:
        x = nx
        y = ny

print(x+1, y+1)