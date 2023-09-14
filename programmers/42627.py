# 힙
# 디스크 컨트롤러

import heapq


# SJF 알고리즘
def solution(jobs):
    answer = []
    n = len(jobs)

    jobs.sort()  # 요청 시간순 정렬
    n = len(jobs)

    now = 0  # 현재 시각
    pre = -1  # 직전 작업이 끝난 시각

    waiting = []  # 대기중인 프로세스를 저장하는 힙

    # 종료된 프로세스 수가 n이 될 때까지 반복
    while len(answer) < n:
        for job in jobs:
            # '직전 작업~현재' 사이에 요청된 job이 있으면
            if pre < job[0] <= now:
                # 대기 힙에 소요시간이 짧은 순으로 저장 (최소힙)
                heapq.heappush(waiting, (job[1], job[0]))  # (소요시간, 입력시각)

        # 대기중인 작업이 있으면
        if waiting:
            new = heapq.heappop(waiting)  # 가장 소요시간이 짧은 작업
            pre = now  # 앞 작업이 끝난 시간 기록
            now += new[0]  # 새로운 작업의 소요시간만큼 시간 경과
            answer.append(now - new[1])  # 종료 시각 - 입력 시각
        # 대기중인 작업이 없으면
        else:
            now += 1  # 1초씩 증가

    return sum(answer) // n