# 힙
# 더 맵게

import heapq


def solution(scoville, K):
    answer = 0
    heap = []

    # 스코빌 목록을 힙에 담기
    for s in scoville:
        heapq.heappush(heap, s)

    # K보다 작은 값이 힙에 하나라도 있다면
    while any(K > i for i in heap):
        # 불가능한 경우
        if len(heap) < 2:
            return -1

        # 문제에서 제시한 연산
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second * 2)
        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
# 2
