# DP
# 도둑질

def solution(money):
    n = len(money)

    if n == 3:
        return max(money)

    # i가 0이면 첫번째 집 불포함, 1이면 포함
    dp = [[0] * n for _ in range(2)]

    dp[0][0], dp[0][1] = 0, money[1]
    dp[1][0], dp[1][1] = money[0], money[0]

    # 2~n-1번째 집 DP 연산
    for i in range(2, n - 1):
        # max(한칸 앞까지 최대값, 두칸 앞까지 최댓값 + 현재 값)
        dp[0][i] = max(dp[0][i - 1], dp[0][i - 2] + money[i])
        dp[1][i] = max(dp[1][i - 1], dp[1][i - 2] + money[i])

    # 첫번째 집 불포함 -> 마지막 값은 max 연산 수행
    dp[0][-1] = max(dp[0][-2], dp[0][-3] + money[-1])
    # 첫번째 집 포함 -> 마지막 집 불포함
    dp[1][-1] = dp[1][-2]

    return max(dp[0][-1], dp[1][-1])