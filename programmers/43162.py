# DFS 깊이 우선 탐색
# 네트워크

# 2차 풀이
def dfs(num, computers, visited):
    for idx, connected in enumerate(computers[num]):
        # 연결되어있지만 아직 방문하지 않았다면
        if connected and not visited[idx]:
            # 방문 기록하기
            visited[idx] = True
            # 깊이우선탐색
            dfs(idx, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        # 이미 방문한 컴퓨터라면
        if visited[i]:
            continue

        # 첫 방문이라면
        answer += 1
        dfs(i, computers, visited)

    return answer

'''
# 1차 풀이
def dfs(j, computers, visited):
    visited[j] = True
    for k in range(len(computers[0])):
        if not visited[k] and computers[j][k]:
            dfs(k, computers, visited)
    return visited


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        for j in range(n):
            if not visited[j] and computers[i][j]:
                visited = dfs(j, computers, visited)
                answer += 1

    print(answer)
    return answer
'''

solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])
# 1
