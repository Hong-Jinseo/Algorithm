# 그래프
# 순위

# 2차 풀이
def solution(n, results):
    # graph[A가][B에게] = 졌다/이겼다
    graph = [[0] * (n) for _ in range(n)]

    for a, b in results:
        graph[a - 1][b - 1] = 1  # a가 b를 이겼다
        graph[b - 1][a - 1] = -1  # b가 a에게 졌다

    for now in range(n):
        # 현재 플레이어가 이긴 사람의 목록
        # -> 현재 플레이어는 players보다 강하다, players가 이긴 사람들보다도 강하다
        players = [i for i, rst in enumerate(graph[now]) if rst == 1]

        # now가 이긴 사람들을 전부 처리할 때까지
        while players:
            p = players.pop()

            for i, rst in enumerate(graph[p]):
                # 이겼는데 결과가 기록되지 않았다면
                if rst == 1 and graph[now][i] == 0:
                    graph[now][i] = 1   # 결과 기록
                    graph[i][now] = -1
                    players.append(i)   # now가 이긴 사람의 목록에 추가

    return [g.count(0) == 1 for g in graph].count(True)

'''
# 1차 풀이
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
'''