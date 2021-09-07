#주울 수 있는 최대의 돈

"""
[입력]
8
1 2 3 4 5 6 7 8

[출력]
27
"""

def solution(n, Money):
    dp = [0] * 30001
    dp[1] = Money[0]
    
    if n > 1 :
        dp[2] = Money[0] + Money[1]
        
    if n > 2 :
        for i in range(3, n+1):
            # 최댓값(N-1번까지의 돈, N-2번까지의 돈과 N번째 돈, N-3번까지의 돈과 N-1 & N번째 돈)
            dp[i] = max(dp[i-1], dp[i-2]+Money[i-1], dp[i-3]+Money[i-2]+Money[i-1])
        
    return dp[n]


def main():
    n = int(input())
    M = [int(x) for x in input().split()]
    print(solution(n,M))
	
	
main()
