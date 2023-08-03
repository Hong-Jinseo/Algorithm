# DP
# 정수 삼각형

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

d = [[0] * n for _ in range(n)]
d[0][0] = graph[0][0]


for i in range(1, n):
    for j in range(0, i+1):
        a = 2
        d[i][j] = graph[i][j] + max(d[i-1][j-1], d[i-1][j])

print(max(d[n-1]))


'''
7               0
3 8            0 1
8 1 0         0 1 2
2 7 4 4      0 1 2 3
4 5 2 6 5   0 1 2 3 4
'''

