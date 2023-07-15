# 구현 (+ 재귀)
# 괄호 변환


# 문자열을 u와 v로 나누는 기준점을 반환하는 함수
def partitions(p):
    partition = 0
    left, right = 0, 0

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            partition = i
            break

    return partition


# '올바른 괄호 문자열'인지 확인하는 함수
def check_right(p):
    stack = []
    for value in p:
        # 열린 괄호
        if value == '(':
            stack.append(value)
        # 닫힌 괄호
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    if stack:
        return False

    else:
        return True


# 문자열의 괄호 방향을 뒤집는 함수
def reverse(lst):
    result = ''
    for i in lst:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result


def solution(p):
    answer = ''

    paren = list(p)
    stack = []

    while paren:
        pt = partitions(paren)

        u = paren[:pt+1]
        v = paren[pt+1:]

        if check_right(u):
            answer += ''.join(u)
        else:
            answer += '('
            # 문자열 v를 작업한 후 u를 이어붙어야 하기 때문에 (4-2)
            # '올바른 괄호 문자열'이 아닌 u를 stack에 넣음
            stack.append(u)
            stack.append(')')

        paren = v

    # '올바른 괄호 문자열'이 아닌 u를 뒤에 덧붙이는 과정 (4)
    while stack:
        if stack[-1] == ')':        # (4-3)
            answer += stack.pop()
        else:                       # (4-4)
            temp = reverse(stack.pop())
            answer += temp[1:-1]

    return answer


print(solution(input()))
