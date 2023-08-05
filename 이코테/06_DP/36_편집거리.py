# DP
# 편집 거리

def edit_dist(str1, str2):
    n = len(str1)   # 수정값
    m = len(str2)   # 목표값

    d = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        d[i][0] = i
    for j in range(1, m+1):
        d[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            # 문자가 같다면 -> 변경X
            if str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]

            # 문자가 다르다면
            else:
                # d[i][j] = min(삽입, 삭제, 교체)
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
    return d[n][m]


a = input()
b = input()
print(edit_dist(a, b))
