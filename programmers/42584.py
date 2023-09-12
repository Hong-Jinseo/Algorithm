# 스택
# 주식가격

from collections import deque


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [(prices[0], 0)]
    prices = deque(prices[1:])
    idx = 1

    while prices:
        now = prices.popleft()
        while stack and stack[-1][0] > now:
            out = stack.pop()
            answer[out[1]] = idx - out[1]
        stack.append((now, idx))
        idx += 1

    while stack:
        out = stack.pop()
        answer[out[1]] = n - out[1] - 1

    return answer


print(solution([1, 2, 3, 2, 3]))
# [4, 3, 1, 1, 0]
