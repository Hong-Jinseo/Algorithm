# 큐
# 같은 숫자는 싫어

def solution(arr):
    answer = []

    pre = arr[0]
    answer.append(pre)
    for now in arr[1:]:
        if pre != now:
            answer.append(now)
            pre = now

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
# [1, 3, 0, 1]
