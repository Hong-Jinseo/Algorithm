# 스택
# 올바른 괄호

def solution(s):
    stack = []

    for now in s:
        # 열린 괄호일 때
        if now == "(":
            stack.append(now)  # 스택에 저장
        # 닫힌 괄호일 때
        else:
            # 스택이 비었거나, 스택에서 닫힌 괄호가 나온다면
            if not stack or stack.pop() == now:
                return False

    # 스택에 괄호가 남아있다면
    if stack:
        return False
    return True
