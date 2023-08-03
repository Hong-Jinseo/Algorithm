# DP
# 금광

t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    # 입력받은 금광 정보를 2차원 배열로 저장
    graph = []
    for i in range(0, n*m, m):
        graph.append(lst[i:i+m])

    d = [[0] * (m+1) for _ in range(n+1)]
    for j in range(n):
        d[j][0] = graph[j][0]

    for i in range(1, m):
        for j in range(1, n):
            # 누적 금 양 = 해당 위치의 금의 수 + max(왼쪽 아래, 왼쪽, 왼쪽 위 누적)
            d[j][i] = graph[j][i] + max(d[j-1][i-1], d[j][i-1], d[j+1][i-1])

    result.append(max(d[i][m-1] for i in range(1, n)))

for data in result:
    print(data)
