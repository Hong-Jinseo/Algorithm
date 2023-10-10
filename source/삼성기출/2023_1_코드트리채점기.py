# 코드트리 채점기
# https://www.codetree.ai/training-field/frequent-problems/problems/codetree-judger

# 시간초과 코드 (토론에 올라온 테스트케이스는 전부 통과)

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

q = int(input())  # 명령어 수
sign, n, url = input().split()
n = int(n)

waiting = {}            # 채점 대기 큐
judging = [False] * n   # 채점 중
history = {}            # 채점 완료
url_in_judging = {}     # 현재 채점 중인 도메인

# 첫 번째 명령
d, u = url.split('/')
waiting[d] = []
heapq.heappush(waiting[d], (1, 0, int(u)))  # waiting[도메인] = [[우선순위, 입력시간, 문제번호], ...]

for _ in range(q - 1):
    order = list(input().split())
    sign = order[0]

    # 채점 요청
    if sign == '200':
        t, p, u = int(order[1]), int(order[2]), order[3]  # t초, 우선순위, url
        domain, num = u.split('/')
        num = int(num)

        # 이전에 입력된 적 있고, 현재 대기 큐에 있는 url이라면
        if domain in waiting and any(w for w in waiting[domain] if w[2] == num):
            continue

        if domain in waiting:
            heapq.heappush(waiting[domain], (p, t, num))
        else:
            waiting[domain] = [(p, t, num)]


    # 채점 시도
    elif sign == '300':
        t = int(order[1])

        if all(judging):
            continue

        target = [INF, INF, '']  # 우선순위, 입력시간, 도메인

        for domain in waiting:
            if len(waiting[domain]) < 1:
                continue

            # 해당 task의 도메인이 현재 채점을 진행중인 도메인 중 하나라면 불가능합니다.
            if domain in url_in_judging and url_in_judging[domain] == True:
                continue

            # 현재 시간 t가, 가장 최근 채점된 도메인의 start+3×gap 보다 작다면
            if domain in history:
                if t < history[domain][0] + 3 * (history[domain][1] - history[domain][0]):
                    continue

            # 가능성이 있는 도메인이라면
            p, start, number = waiting[domain][0]

            # target = [우선순위, 입력시간, 도메인]
            if p < target[0]:
                target = [p, start, domain]
            elif p == target[0] and start < target[1]:
                target = [p, start, domain]

        if len(target[-1]) > 0:
            # 가장 우선순위가 높은 task
            heapq.heappop(waiting[target[-1]])
            target_d = target[-1]

            # 채점
            for i, judge in enumerate(judging):
                # 쉬고 있는 채점기가 있다면
                if not judge:
                    # 채점 진행
                    judging[i] = (t, target_d)
                    url_in_judging[target_d] = True

                    break


    # 채점 종료
    elif sign == '400':
        end, J_id = int(order[1]), int(order[2])
        J_id -= 1

        # 해당 채점기가 채점중인 url이 있었다면
        if judging[J_id]:
            start, domain = judging[J_id]

            # 채점 종료
            judging[J_id] = False
            url_in_judging[domain] = False

            # 채점 완료 목록 갱신
            history[domain] = [int(start), int(end)]


    # 채점 대기 큐 조회
    else:
        count = 0
        for d in waiting:
            if len(waiting[d]) > 0:
                count += len(waiting[d])
        print(count)

