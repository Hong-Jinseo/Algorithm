# 해시
# 폰켓몬

def solution(nums):
    s = set(nums)
    if len(s) >= len(nums) / 2:
        return len(nums) / 2
    else:
        return len(s)


print(solution([3, 1, 2, 3]))
