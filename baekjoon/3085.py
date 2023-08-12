# 부르트 포스
# 사탕 게임

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input()) * n for _ in range(n)]


# 먹을 수 있는 사탕
def count(graph, n):
    row_max, row_cnt, col_max, col_cnt = -1, 1, -1, 1
    # 행
    for i in range(n):
        for j in range(n-1):
            if graph[i][j] == graph[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    # 열
    for j in range(n):
        for i in range(n-1):
            if graph[i][j] == graph[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1

    return max(row_max, col_max)


result = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            cnt = count(graph, n)
            result = max(result, cnt)
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

        if i+1 < n:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            cnt = count(graph, n)
            result = max(result, cnt)
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]

print(result)
