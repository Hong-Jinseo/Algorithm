# DFS 깊이 우선 탐색
# 타겟 넘버

# dfs(숫자 배열, 현재까지 누적 값, 인덱스, 타겟값, 타겟을 달성한 횟수)
def dfs(arr, now, index, target, count):
    # 마지막 숫자까지 처리했다면
    if index == len(arr):
        return count + 1 if now == target else count

    count = dfs(arr, now + arr[index], index + 1, target, count)
    count = dfs(arr, now - arr[index], index + 1, target, count)

    return count


def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target, 0)
    print(answer)

    return answer