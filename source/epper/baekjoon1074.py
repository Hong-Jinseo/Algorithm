# Z모양

"""
[입력]      [출력]
2 3 1       11

[입력]      [출력]
3 7 7       63
"""

def solution(n,r,c):
    answer = 0
    width = 2**n
    area = width**2

    while area!=1:
        #1,2사분면
        if r <= ((width/2)-1):
            #1사분면
            if c > ((width/2)-1):
                answer += area/4
                c -= width/2
        #3,4사분면
        else:
            r -= width/2
            #4사분면
            if c > ((width/2)-1):
                answer += area/4 * 3
                c -= width/2
            #3사분면
            else:
                answer += area/4 * 2

        width /= 2
        area /= 4

    answer = int(answer)
    return answer


n, r, c = map(int, input().split())
print(solution(n,r,c))
