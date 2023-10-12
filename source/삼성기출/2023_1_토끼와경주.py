# 토끼와 경주
# https://www.codetree.ai/training-field/frequent-problems/problems/rabit-and-race

import heapq
import sys
input = sys.stdin.readline


# 좌표 찾기
def find_next(MAX, now):
    now %= 2 * (MAX - 1)
    return min(now, 2 * (MAX - 1) - now)


# 경주 진행 함수 (라운드, 점수)
def second(r, s):
    # 참가여부 초기화
    for k in rabbits:
        joined[k] = False

    total_score = 0
    selected_rabbit = []

    # 라운드 시작
    for pp in range(r):
        temp = []
        rb = heapq.heappop(priority)

        move = distances[rb[-1]]
        dx = [move, -move, 0, 0]
        dy = [0, 0, move, -move]

        # 토끼 현재 좌표
        x, y = rb[2], rb[3]

        # 토끼가 이동 가능한 경우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            nx = nx if 0 <= nx < N else find_next(N, nx)
            ny = ny if 0 <= ny < M else find_next(M, ny)

            temp.append((nx + ny, nx, ny))

        # 토끼 최종 좌표
        temp.sort(key=lambda x: (-x[0], -x[1], -x[2]))

        # (이동거리, x+y, x, y, 고유번호, 참가여부)
        heapq.heappush(priority, [rb[0] + 1, temp[0][0], temp[0][1], temp[0][2], rb[-1]])  # 최소힙
        heapq.heappush(selected_rabbit, [-temp[0][0], -temp[0][1], -temp[0][2], -rb[-1]])  # 최대힙

        joined[rb[-1]] = True

        # 해당 토끼의 점수 빼고 + 모든 토끼의 점수 한 번에 증가
        scores[rb[-1]] -= temp[0][0] + 2
        total_score += temp[0][0] + 2

    # 라운드 종료 후, 점수 계산
    # 최종 우선순위 (뽑혔는지 여부 1, 행+열 내림차순, 행 내림차순, 열 내림차순, 고유번호 내림차순)
    first_place = heapq.heappop(selected_rabbit)

    # 참가 경험이 있는 토끼라면
    if joined[-first_place[-1]]:
        scores[-first_place[-1]] += s

    return total_score


# 입력 받기
Q = int(input())

# 첫 번째 명령
first = list(map(int, input().split()))
N, M, P = first[1], first[2], first[3]

distances = {}  # 이동거리
scores = {}  # 점수
rabbits = []
joined = {}  # 참가여부

score_sum = 0

for i in range(4, P * 2 + 4, 2):
    key = first[i]
    dist = first[i + 1]

    rabbits.append(key)
    distances[key] = dist
    scores[key] = 0
    joined[key] = False


# 토끼들의 우선순위 기록 (총 점프 횟수, 행+열, 행, 열, 고유번호, 선발여부)
priority = []
for rabbit in rabbits:
    heapq.heappush(priority, [0, 0, 0, 0, rabbit])


for _ in range(Q - 1):

    order = list(map(int, input().split()))
    sign = order[0]

    # 경주 진행
    if sign == 200:
        score_sum += second(order[1], order[2])

    # 이동거리 변경
    elif sign == 300:
        if order[1] in distances:
            distances[order[1]] *= order[2]

    # # 최고의 토끼 선정
    elif sign == 400:
        print(max(i for i in scores.values()) + score_sum)
