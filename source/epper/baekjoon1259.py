# 팰린드롬수

"""
121
1231
12421
0
"""

def solution(num):

    oriNum = []

    for i in num:
        oriNum.append(i)
    
    for i in range(len(num)):
        if(oriNum[i] != oriNum[len(oriNum)-i-1]):
            return "No"
    return "Yes"


if __name__=='__main__':

    while True:
        num = input()

        if num == '0':
            break
        
        print(solution(num))
