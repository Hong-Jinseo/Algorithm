# 이진탐색
# 징검다리


def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()

    # 이진탐색 기준: 각 지점 사이의 거리의 최솟값
    left, right = 0, distance

    while left <= right:
        mins = int(1e9)  # 각 지점 사이의 거리의 최솟값
        pre = 0  # 앞에 있는 바위의 위치
        removed = 0  # 삭제할 돌의 개수

        # mid보다 좁은 간격이라면 해당 바위 삭제
        mid = (left + right) // 2

        for cur in rocks:
            # 현재 바위와 앞 바위의 간격이 mid보다 작다면 -> 제거
            if cur - pre < mid:
                removed += 1
            else:
                mins = min(mins, cur - pre)
                pre = cur

        # removed: 각 지점 사이의 거리의 최솟값이 mid일 때 제거한 바위의 수
        # n: 목표하는 제거할 바위의 수

        if removed > n:
            # 바위를 덜 제거해야 함 -> 간격 좁히기
            right = mid - 1
        else:
            # 동일 or 더 제거해야 함 -> 간격 늘리기
            left = mid + 1
            answer = mins

    return answer
