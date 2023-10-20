# 그래프
# 순위

def solution(n, results):
    result = [[0] * n for _ in range(n)]
    WIN, LOSE = 1, -1

    for a, b in results:
        result[a - 1][b - 1] = WIN  # a가 b를 이겼다
        result[b - 1][a - 1] = LOSE  # b가 a에게 졌다

    for player in range(n):
        # player가 이긴 사람 목록
        wins = [opp for opp, rst in enumerate(result[player]) if rst == WIN]

        while wins:
            loser = wins.pop()
            for opp, rst in enumerate(result[loser]):
                if rst == WIN and result[player][opp] == 0:
                    result[player][opp], result[opp][player] = WIN, LOSE
                    wins.append(opp)

    return len(['know' for x in result if x.count(0) == 1])
