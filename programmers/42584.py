# 스택
# 주식가격

def solution(prices):
    result = []
    stack = [[prices[0], 0]]
    cnt = 0

    for i, p in enumerate(prices[1:], start=1):
        cnt += 1
        # 스택에 본인보다 큰 값이 있으면 pop
        while stack and stack[-1][0] > p:
            val, idx = stack.pop()
            result.append((idx, cnt - idx)) # pop한 값을 저장 (input순서, pop까지 소요시간)

        stack.append([p, i])
    
    while stack:
        val, idx = stack.pop()
        result.append((idx, cnt - idx))
    
    result.sort()   # result를 sort하는 대신, 미리 리스트[0]*n 만들어놓고 삽입하는 것도 가능

    return [row[1] for row in result]

print(solution([1, 2, 3, 2, 3]))
# [4, 3, 1, 1, 0]
