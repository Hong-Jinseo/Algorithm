# 스택
# 올바른 괄호

def solution(s):
    stack = list()

    for brace in s:
        if brace == '(':
            stack.append(brace)
        elif stack :
            # input이 )인 경우
            top = stack.pop()
            if top != '(':
                return False
        else:
            # input이 )인데 stack이 비어있는 경우
            return False
        
        ''' # 조건문 개선
        if brace == '(':
            stack.append(brace)
        elif (not stack or stack.pop() == brace):
            return False
        '''
    
    # 스택에 괄호가 남아있다면
    if stack:
        return False
    return True

print(solution(")()("))

'''
"()()"	true
"(())()"	true
")()("	false
"(()("	false
'''