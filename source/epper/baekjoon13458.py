#시험 감독

"""
[입력]
5
1000000 1000000 1000000 1000000 1000000
5 7

[출력]
713290
"""
        
def solution(A, b, c):
    answer = 0
    for i in range(len(A)):
        num = int(A[i])-b
        answer += 1             #총감독관
        #부감독관이 꼭 필요한지 확인
        if num>0:
            answer += num//c    #부감독관
            if num%c != 0:
                answer += 1     #부감독관(응시자가 나누어 떨어지지 않는 경우)
    
    return answer


n = int(input())
temp = input()
A = temp.split()
b, c = input().split()

b = int(b)
c = int(c)

print(solution(A, b, c))