# 브루트 포스
# N과 M (1)

def dfs(a):
    if a == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            dfs(a - 1)
            answer.pop()
            visited[i] = False


n, m = map(int, input().split())
visited = [False] * (n+1)
answer = []
dfs(m)
