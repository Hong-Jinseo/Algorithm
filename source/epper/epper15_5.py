#문자열 압축
"""
[입력]
00000000111111111111111111111111110000000000000000

[출력]
HZP
"""

def solution(user_input):

    answer = ""
    cnt = 65
    
    if user_input[0] == "1":
        answer += "1"

    for i in range(1, len(user_input)):
        if user_input[i] == user_input[i-1]:
            cnt += 1                   
        else:
            answer += chr(cnt)
            cnt = 65

        if i == len(user_input)-1:
            answer += chr(cnt)
    
    return answer


user_input = input()
print(solution(user_input))
