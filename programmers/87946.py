# 완전탐색
# 피로도

from itertools import permutations


def solution(k, dungeons):
    answer = -1
    n = len(dungeons)

    # 전체 던전을 가능한 모든 조합으로 나열
    for lst in permutations(dungeons, n):
        now = k     # 현재 피로도
        count = 0   # 탐험 가능한 던전 수

        # 최소 필요 피로도, 소모 피로도
        for need, spent in lst:
            if need <= now:
                now -= spent
                count += 1

        answer = max(answer, count)

    return answer
