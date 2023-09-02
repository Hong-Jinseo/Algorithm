# 해시
# 폰켓몬

def solution(nums):
    return min(len(set(nums)), int(len(nums)/2))


print(solution([3, 1, 2, 3]))
