# 깊이/너비 우선 탐색(DFS/BFS)
# 타겟 넘버

# (연산 횟수, 숫자길이, 숫자목록, 목표 결과, 앞 연산 결과)
def dfs(cnt, length, numbers, target, result):
    answer = 0
    if cnt == length:
        if result == target:
            return True
        return False

    answer += dfs(cnt+1, length, numbers, target, result + numbers[cnt])
    answer += dfs(cnt+1, length, numbers, target, result - numbers[cnt])
    
    return answer


def solution(numbers, target):
    answer = dfs(0, len(numbers), numbers, target, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
# 5


'''
# 2차 풀이
def dfs(nums, idx, total, target, cnt):
    if idx == len(nums):
        return cnt + 1 if total == target else cnt

    cnt = dfs(nums, idx + 1, total + nums[idx], target, cnt)
    cnt = dfs(nums, idx + 1, total - nums[idx], target, cnt)

    return cnt


def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target, 0)
    return answer


# 1차 풀이
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
'''
