# 그리디
# 큰 수 만들기

def solution(number, k):
    stack = []  # 가장 큰 숫자를 저장할 스택

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    return ''.join(stack[:len(stack) - k])
