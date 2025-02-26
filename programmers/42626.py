# 힙
# 더 맵게

import heapq

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    # 최소값이 K 미만이면
    while scoville[0] < K:
        # 2개 미만이면 더이상 연산 불가
        if len(scoville) < 2:
            answer = -1
            break

        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
# 2
