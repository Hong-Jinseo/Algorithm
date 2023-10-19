# 이진탐색
# 입국심사

def solution(n, times):
    left = 0
    right = n * max(times)

    while left < right:
        # 이진탐색
        mid = (left + right) // 2
        count = 0

        # mid초까지 각 심사관이 몇 명을 처리할 수 있는지 체크
        for t in times:
            count += mid // t

        # 시간 내 심사한 사람이 목표보다 적다면 -> 시간 연장 (mid+1초 ~ right초)
        if count < n:
            left = mid + 1

        # 시간 내 심사한 사람이 목표보다 많다면 -> 시간 단축 (left초 ~ mid초)
        else:
            right = mid

    return left
