# 나무박멸 (22년 상반기)
# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/


n, m, k, c = map(int, input().split())
trees = [list(map(int, input().split())) for _ in range(n)]

herbicide = [[0] * n for _ in range(n)]  # 제초제

# 상하좌우, 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


# 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 나무가 퍼질 수 있는 칸인지 체크
def can_plant(x, y):
    space = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어난다면
        if not in_range(nx, ny):
            continue

        # 벽, 다른 나무, 제초제가 없다면
        if trees[nx][ny] == 0 and not herbicide[nx][ny]:
            space.append((nx, ny))

    return space


# 주위의 나무 세기
def count_near_tree(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어난다면
        if not in_range(nx, ny):
            continue

        # 나무가 있다면
        if trees[nx][ny] > 0:
            count += 1

    return count


# 죽일 수 있는 나무의 수 세기
def count_kill(x, y):
    # 성이나 나무가 없는 곳이라면
    if trees[x][y] <= 0:
        return (0, [])

    total = trees[x][y]
    route = [(x, y)]

    # 대각선 탐색
    for i in range(4, 8):
        nx = x + dx[i]
        ny = y + dy[i]

        count = k

        # 맵을 벗어나지 않고 and 벽이 아니라면
        # while in_range(nx, ny) and trees[nx][ny] and count > 0:
        while in_range(nx, ny) and trees[nx][ny] != -1 and count > 0:
            count -= 1

            total += trees[nx][ny]
            route.append((nx, ny))

            if trees[nx][ny] == 0:
                break

            nx += dx[i]
            ny += dy[i]

    return (total, route)


# 3. 제초제 뿌리기
def spray():
    # 제초제 뿌릴 칸 찾기
    max_kill, max_x, max_y = 0, 0, 0
    route = []

    for i in range(n):
        for j in range(n):
            new, new_route = count_kill(i, j)

            # 최댓값 갱신
            if max_kill < new:
                max_kill = new
                max_x, max_y = i, j
                route = new_route

    # 제초제 뿌리기
    for kx, ky in route:
        herbicide[kx][ky] = c + 1
        trees[kx][ky] = 0

    return max_kill


# 2. 나무 번식
def plant():
    temp = [[0] * n for _ in range(n)]

    # 나무를 심을 수 있는 공간 체크
    for i in range(n):
        for j in range(n):
            # 나무가 없거나 벽이라면 pass
            if trees[i][j] <= 0:
                continue

            around = can_plant(i, j)

            # 주위에 공간이 없다면
            if not around:
                continue

            # 심을 나무 개수
            cnt = trees[i][j] // len(around)

            # 주위 공간에 심을 나무 기록
            for ax, ay in around:
                temp[ax][ay] += cnt

    # 나무 심기
    for i in range(n):
        for j in range(n):
            trees[i][j] += temp[i][j]


# 1. 나무 성장
def grow():
    for i in range(n):
        for j in range(n):
            # 나무가 있고 and 제초제가 뿌려지지 않았다면
            if trees[i][j] > 0 and not herbicide[i][j]:
                trees[i][j] += count_near_tree(i, j)


# 0. 제초제 상태 갱신
def decrease():
    for i in range(n):
        for j in range(n):
            if herbicide[i][j] > 0:
                herbicide[i][j] -= 1


answer = 0

for iii in range(m):
    # 0. 제초제 상태 갱신
    decrease()

    # 1. 나무 성장
    grow()

    # 2. 나무 번식
    plant()

    # 3. 제초제 뿌리기
    answer += spray()

'''
for aa in range(m):

    target = m-1

    # 0. 제초제 상태 갱신
    decrease()

    if aa == target:
        print('0. 나무 초기 상태')
        for h in trees:
            print(h)
        print()

        print('0. 제초제 초기 상태')
        for h in herbicide:
            print(h)
        print()

    # 1. 나무 성장
    grow()
    if aa == target: 
        print("1. 나무 성장")
        for t in trees:
            print(t)
        print()

    # 2. 나무 번식
    plant()
    if aa == target: 
        print("2. 나무 번식")
        for t in trees:
            print(t)
        print()

    # 3. 제초제 뿌리기
    answer += spray()
    if aa == target: 

        print('0. 제초제 뿌린 후 제초제 상태')
        for h in herbicide:
            print(h)
        print()

        print("3. 제초제 뿌린 후 나무 상태")
        for t in trees:
            print(t)
        print()
'''

print(answer)