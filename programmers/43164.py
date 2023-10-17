# 1차 BFS, 2차 DFS
# 여행경로


# 2차 풀이 : DFS (효율 더 좋음)
def dfs(now, tickets, used, route):
    # 모든 티켓을 사용했다면
    if all(used):
        return True

    for i, ticket in enumerate(tickets):
        # 사용하지 않은 티켓의 출발지가 현위치와 같다면
        if now == ticket[0] and not used[i]:
            route.append(ticket[1])
            used[i] = True

            if dfs(ticket[1], tickets, used, route):
                return route

            route.pop()
            used[i] = False

    return False


def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    used = [False] * len(tickets)

    # 출발지, 티켓목록, 사용여부, 경로, 정답 유무
    route = ['ICN']
    answer = dfs('ICN', tickets, used, route)

    return answer

'''
# 1차 풀이 : BFS
from collections import deque


def solution(tickets):
    answer = []
    # 같은 출발지를 모으고, 도착지 알파벳순 정렬
    tickets.sort(key=lambda x: (x[0], x[1]))

    # bfs
    q = deque([(['ICN'], tickets)])  # (현재까지의 경로, 남은 티켓)

    while q:
        pathN, ticketN = q.popleft()

        # 남은 티켓이 없다면 -> 경로 확정
        if len(ticketN) == 0:
            answer = pathN
            break

        # idx = 현재 있는 공항에서 출발하는 티켓
        idx = -1
        for i in range(len(ticketN)):
            if ticketN[i][0] == pathN[-1]:
                idx = i
                break

        # 출발 가능한 공항이 없으면 -> 불가능한 경우
        if idx == -1:
            continue

        # 현재 있는 공항에서 출발 가능한 티켓일 때
        while idx < len(ticketN) and ticketN[idx][0] == pathN[-1]:
            # ([현재까지의 경로] + [현재 공항에서 갈 수 있는 공항], [idx를 제외한 티켓 리스트])
            q.append((pathN + [ticketN[idx][1]], ticketN[:idx] + ticketN[idx + 1:]))
            # 다음 티켓 확인
            idx += 1

    return answer
'''