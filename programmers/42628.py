# 힙
# 이중우선순위큐

import heapq


def solution(operations):
    min_h = []  # 최소힙
    max_h = []  # 최대힙
    length = 0  # 힙에 저장된 원소의 개수

    for op in operations:
        # 입력 연산
        if op[0] == 'I':
            heapq.heappush(min_h, int(op[2:]))
            heapq.heappush(max_h, -int(op[2:]))
            length += 1

        # 최댓값 삭제
        elif max_h and len(op) == 3:
            heapq.heappop(max_h)
            length -= 1

        # 최솟값 삭제
        elif min_h and len(op) == 4:
            heapq.heappop(min_h)
            length -= 1

        # 우선순위 큐가 비었다면 -> 최대힙, 최소힙 초기화
        if length == 0:
            max_h = []
            min_h = []

    # 힙에 값이 남아있다면, 최댓값과 최솟값을 각각 M과 m에 저장
    M = -heapq.heappop(max_h) if max_h else -1e9
    m = heapq.heappop(min_h) if min_h else 1e9

    if M >= m:
        return [M, m]
    else:
        return [0, 0]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
# [333, -45]
