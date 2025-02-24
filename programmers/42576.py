# 해시
# 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    result = p - c
    for v in result:
        return v

    # [참고] 다음과 같이 return 쓰면 됨
    # return next(iter(result))  # result에서 첫 번째 요소를 반환 (키 값만 필요)

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))