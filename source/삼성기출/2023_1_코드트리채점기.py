# 코드트리 채점기
# https://www.codetree.ai/training-field/frequent-problems/problems/codetree-judger

# 시간초과 코드 (토론에 올라온 테스트케이스는 전부 통과)

import sys

input = sys.stdin.readline

import heapq
from collections import deque


# url에서 도메인만 추출하는 함수
def find_domain(url):
    temp = list(url.split('/'))
    return temp[0]


q = int(input())  # 명령어 수
sign, n, url = input().split()
n = int(n)

waiting = []  # 채점 대기 큐
judging = [False] * n  # 채점 중
history = {}  # 채점 완료
url_in_waiting = {}  # 현재 대기 중인 도메인
url_in_judging = {}  # 현재 채점 중인 도메인

# 첫 번째 명령
heapq.heappush(waiting, (int(n), url, 0, find_domain(url)))  # 우선순위, 시작시간(입력시간), 도메인
url_in_waiting[find_domain(url)] = True

for _ in range(q - 1):
    order = list(input().split())
    sign = order[0]

    # 채점 요청
    if sign == '200':
        t, p, u = int(order[1]), int(order[2]), order[3]  # t초, 우선순위, url
        domain = find_domain(u)

        # 단, 채점 대기 큐에 있는 task 중 정확히 u와 일치하는 url이 단 하나라도 존재한다면 큐에 추가하지 않고 넘어갑니다.
        # 이전에 입력된 적 있고, 현재 대기 큐에 있는 url이라면
        if u in url_in_waiting and url_in_waiting[u] == True:
            continue

        else:
            url_in_waiting[u] = True
            heapq.heappush(waiting, (p, u, t, domain))


    # 채점 시도
    elif sign == '300':
        t = int(order[1])
        tasks = []

        while waiting:
            task = heapq.heappop(waiting)
            tasks.append(task)

            p, u, start, domain = task
            # t = int(t)

            # 해당 task의 도메인이 현재 채점을 진행중인 도메인 중 하나라면 불가능합니다.
            if domain in url_in_judging and url_in_judging[domain] == True:
                continue

            # 해당 task의 도메인과 정확히 일치하는 도메인, 가장 최근 된 채점 시작 시간이 start, 종료 시간이 start+gap 였고
            # 현재 시간 t가 start+3×gap 보다 작다면
            if domain in history:
                # print(history[domain][0], history[domain][1])
                # continue
                if t < history[domain][0] + 3 * (history[domain][1] - history[domain][0]):
                    continue

            for i, judge in enumerate(judging):
                # 쉬고 있는 채점기가 있다면
                if not judge:
                    # 대기 큐에서 삭제
                    url_in_waiting[u] = False
                    tasks.pop()

                    # 채점 진행
                    judging[i] = (t, task[2], i, domain)  # 시작시간, url, 채점기 번호, 도메인
                    url_in_judging[domain] = True

                    break
            break

        # 우선순위는 높았으나 조건에 맞지 않았던 task들
        for t in tasks:
            heapq.heappush(waiting, t)


    # 채점 종료
    elif sign == '400':
        end, J_id = int(order[1]), int(order[2])
        J_id -= 1

        # 해당 채점기가 채점중인 url이 있었다면
        if judging[J_id]:
            start, u, i, domain = judging[J_id]

            # 채점 종료
            judging[J_id] = False
            url_in_judging[domain] = False

            # 채점 완료 목록 갱신
            history[domain] = [int(start), int(end)]


    # 채점 대기 큐 조회
    else:
        print(len(waiting))
