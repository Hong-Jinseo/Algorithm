# DFS 깊이 우선 탐색
# 네트워크

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


solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])
# 1
