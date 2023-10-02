# DP
# 정수 삼각형

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
