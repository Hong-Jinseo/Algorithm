# BFS
# 퍼즐 조각 채우기

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def convert(xys, target):
    default = 1 if target == 0 else 0
    fixed = {i: [] for i in range(1, 7)}
    for i in xys:
        for xy in xys[i]:
            # 좌측 상단 좌표
            lx, ly = min(p[0] for p in xy), min(p[1] for p in xy)
            # 우측 하단 좌표
            rx, ry = max(p[0] for p in xy), max(p[1] for p in xy)

            width = ry - ly + 1
            height = rx - lx + 1

            # 퍼즐이 포함된 최소 사각형 만들기
            temp = [[default] * width for _ in range(height)]
            for x, y in xy:
                temp[x - lx][y - ly] = target

            fixed[i].append(temp)
    return fixed


# 퍼즐 찾기
def bfs_find(a, b, temp, N, group, target):
    q = deque([(a, b)])
    temp[a][b] = 2

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if temp[nx][ny] == target:
                    temp[nx][ny] = 2
                    group.append((nx, ny))
                    q.append((nx, ny))

    # group에 직사각형 데이터가 포함됨


# 회전
def rotate(graph):
    n, m = len(graph), len(graph[0])
    temp = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[j][n - i - 1] = graph[i][j]

    return temp


def is_match(x, y, puzzle, game_board):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if game_board[r + x][c + y] + puzzle[r][c] != 1:
                return False
    return True


def match_puzzle(r, c, frag_dict, visited_board, game_board):
    cnt = 0
    q = deque([(r, c)])
    path = [(r, c)]

    while q:
        x, y = q.popleft()
        cnt += 1
        path.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < len(game_board) and 0 <= ny < len(game_board[0])):
                continue

            if not game_board[nx][ny] and not visited_board[nx][ny]:
                visited_board[nx][ny] = 1
                q.append((nx, ny))

    puzzles = frag_dict[cnt]
    r_min = min([pos[0] for pos in path])
    c_min = min([pos[1] for pos in path])

    for i in range(len(puzzles)):
        puzzle = puzzles[i]
        for _ in range(4):
            puzzle = rotate(puzzle)

            r_len = len(puzzle)
            c_len = len(puzzle[0])

            # 회전한 조각이 board 범위 안 넘어가는지 체크
            if not (0 <= r_min + r_len - 1 < len(game_board) and 0 <= c_min + c_len - 1 < len(game_board[0])):
                continue

            if is_match(r_min, c_min, puzzle, game_board):
                del frag_dict[cnt][i]  # 사용한 조각 제거
                return cnt

    return 0


def solution(game_board, table):
    answer = 0
    n = len(game_board)

    count = 0
    for t in table:
        count += t.count(1)

    # puzzle[i개로 이루어진 퍼즐] = [[해당 퍼즐을 이루는 좌표들], ...]
    puzzle = {i: [] for i in range(1, 7)}

    # 퍼즐 찾기
    for i in range(n):
        for j in range(n):
            # 퍼즐이면
            if table[i][j] == 1:
                group = [(i, j)]
                bfs_find(i, j, table, n, group, 1)
                puzzle[len(group)].append(group)

    # 퍼즐을 직사각형으로 만들기
    fixed_puzzle = convert(puzzle, 1)

    ###### 다른 풀이 참고
    # 보드에 조각 끼워넣기
    visited_board = [[0] * len(game_board) for _ in range(len(game_board[0]))]
    for r in range(len(game_board)):
        for c in range(len(game_board[0])):
            if not game_board[r][c] and not visited_board[r][c]:
                visited_board[r][c] = 1
                answer += match_puzzle(r, c, fixed_puzzle, visited_board, game_board)

    return answer

    '''
    # 빈칸 찾기
    blank = {i: [] for i in range(1, 7)}
    for i in range(n):
        for j in range(n):
            # 빈칸이면
            if game_board[i][j] == 0:
                group = [(i, j)]
                bfs_find(i, j, game_board, n, group, 0)
                blank[len(group)].append(group)

    # 빈칸을 직사각형으로 만들기
    fixed_blank = convert(blank, 0)

    # 4개의 방향에 대해서
    for _ in range(4):
        # 빈칸에 퍼즐 넣어보기
        for idx in range(1, 7):
            # i개의 칸으로 이루어진 공백 공간 blk
            for blk in fixed_blank[idx]:
                blk_h, blk_w = len(blk), len(blk[0])

                # i개의 칸으로 이루어진 퍼즐 rect
                for rect in fixed_puzzle[idx]:
                    rect_h, rect_w = len(rect), len(rect[0])

                    # blk와 rect의 가로세로 길이가 맞으면
                    if blk_w == rect_w and blk_h == rect_h:
                        # 퍼즐 합치기
                        add = [[0] * rect_w for _ in range(rect_h)]
                        for p in range(rect_h):
                            for q in range(rect_w):
                                add[p][q] = blk[p][q] + rect[p][q]

                        # 퍼즐이 맞으면
                        if sum(row.count(1) for row in add) == rect_h * rect_w:
                            if rect in fixed_puzzle[idx] and blk in fixed_blank[idx]:
                                fixed_puzzle[idx].remove(rect)
                                fixed_blank[idx].remove(blk)
                                answer += idx

        # 남아있는 모든 퍼즐 회전
        for key in fixed_puzzle:
            for j, rect in enumerate(fixed_puzzle[key]):
                fixed_puzzle[key][j] = rotate(rect)
    return answer
    '''

'''
# 예외

solution([[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]], [[1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]])
# 73

solution([[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],[[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]])
# 54  
'''
