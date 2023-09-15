# 완전탐색
# 최소직사각형

def solution(sizes):

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    max_w = max([i[0] for i in sizes])
    max_h = max([i[1] for i in sizes])

    return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# 4000
