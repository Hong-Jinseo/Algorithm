# 이진탐색
# 공유기 설치

import sys
input = sys.stdin.readline


def search(a, c, start, end):
    rst = -1
    while start <= end:
        count = 1
        gap = (start + end) // 2
        now = a[0]

        # 공유기 설치 가능한 개수 체크
        for i in range(1, len(a)):
            if a[i] >= now + gap:
                count += 1
                now = a[i]

        # 공유기 개수가 c보다 많거나 같으면 -> 공유기 사이 거리 늘림
        # (가장 인접한 두 공유기 사이의 '최대' 거리를 구해야 하기에 count == c여도 계속 gap 증가시킴)
        if count >= c:
            start = gap + 1
            rst = gap

        # 공유기 개수가 c보다 적으면 -> 공유기 사이 거리 줄임
        else:
            end = gap - 1

    return rst


n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

gap1, gap2 = 1, house[-1] - house[0]

print(search(house, c, gap1, gap2))
