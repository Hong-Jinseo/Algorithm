# 큐
# 프로세스

from collections import deque


def solution(priorities, location):
    count = 0

    priority = []
    for i in range(len(priorities)):
        priority.append((priorities[i], i))
    q = deque(priority)

    while q:
        now = q.popleft()

        # if now보다 우선순위가 높은 프로세스가 큐에 있다면 -> 다시 큐에 넣음
        if any(now[0] < pri[0] for pri in q):
            q.append(now)

        # else 프로세스 실행
        else:
            count += 1
            # 실행한 프로세스가 타겟 프로세스라면
            if now[1] == location:
                return count


print(solution([1, 1, 9, 1, 1, 1], 0))
# 5
