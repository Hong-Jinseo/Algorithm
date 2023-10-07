# 구현
# 달팽이

import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

snail = [[0] * n for _ in range(n)]

i = j = n // 2
snail[i][j] = 1
save = [i+1, j+1]

number, k = 1, 1
direction = 0

while True:
    # 2번 연속으로, k만큼 직진 이동
    for _ in range(2):
        # 직진
        for _ in range(k):
            match direction:
                case 0:
                    i -= 1
                case 1:
                    j += 1
                case 2:
                    i += 1
                case 3:
                    j -= 1

            number += 1
            snail[i][j] = number

            if number == target:
                save = [i+1, j+1]

            # 종료 조건
            if i == 0 and j == 0:
                for s in snail:
                    print(' '.join(list(map(str, s))))
                print(' '.join(list(map(str, save))))
                exit()

        # 방향전환
        direction = direction+1 if direction+1 < 4 else direction-3

    # 반복 횟수 증가
    k += 1
