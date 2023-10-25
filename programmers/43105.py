# DP
# 정수 삼각형

# 2차 풀이
def solution(triangle):
    n = len(triangle)

    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            # 왼쪽 변
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]

            # 오른쪽 변
            elif i == j:
                dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]

            # 내부
            else:
                dp[i][j] = triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[-1])

'''
# 1차 풀이
def solution(triangle):
    n = len(triangle)

    for x in range(1, n):
        # 좌측 값
        triangle[x][0] += triangle[x - 1][0]

        # 우측 값
        triangle[x][x] += triangle[x - 1][x - 1]

        # 중앙 값
        for y in range(1, x):
            triangle[x][y] += max(triangle[x - 1][y - 1], triangle[x - 1][y])

    return max(triangle[n - 1])
'''
