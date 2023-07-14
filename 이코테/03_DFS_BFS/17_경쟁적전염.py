# BFS
# 경쟁적 전염

from collections import deque

n, k = map(int, input().split())
data = []
temp = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            temp.append((data[i][j], 0, i, j))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

temp.sort()
queue = deque(temp)

while queue:
    virus, second, a, b = queue.popleft()

    if second == s:
        break

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                queue.append((virus, second+1, nx, ny))

print(data[x-1][y-1])
