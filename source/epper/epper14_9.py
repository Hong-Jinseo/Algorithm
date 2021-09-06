#주울 수 있는 최대의 돈2 (정수삼각형)

def solution(N, money):
    for i in range(1, N):
        for j in range(i+1):
            if j==0:
                money[i][j] += money[i-1][0]
            elif i==j:
                money[i][j] += money[i-1][j-1]
            else:
                money[i][j] += max(money[i-1][j-1], money[i-1][j])
    return max(money[N-1])



N = int(input())

money = [[0 for i in range(N)] for j in range(N)] 
for i in range(N):
    for j in range(i):
        money[i][j] = input()

print(solution(N, money))
