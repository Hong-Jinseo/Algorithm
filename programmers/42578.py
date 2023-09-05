# 해시
# 의상

from collections import Counter


def solution(clothes):
    answer = 1
    cnt = Counter()

    for item in clothes:
        cnt[item[1]] += 1

    for c in cnt:
        answer *= (cnt[c] + 1)

    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
