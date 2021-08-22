# 팰린드롬수

"""
121
1231
12421
0
"""

def solution(num):

    if num == num[::-1]:
        return "yes"
    else:
        return "no"

if __name__=='__main__':

    num = input()
    
    while num!='0':
        print(solution(num))
        num = input()