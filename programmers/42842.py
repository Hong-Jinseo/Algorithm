# 완전탐색
# 카펫

def solution(brown, yellow):
    brown -= 4  # 모서리 제외
    brown //= 2  # 높이와 너비를 구하기 위해 2로 나눔

    width, height = brown - 1, 1
    area = width * height

    while area != yellow:
        width -= 1
        height += 1
        area = width * height

    return [width + 2, height + 2]


print(solution(10, 2))
# [4, 3]
