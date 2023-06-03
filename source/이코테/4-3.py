# 구현
# 왕실의 나이트



location = input()

loca_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = int(loca_list.index(location[0])) + 1
y = int(location[1])
cnt = 0

# 이동 가능한 모든 경우의 수
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]


for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 < nx < 9 and 0 < ny < 9:
        cnt += 1

print(cnt)
