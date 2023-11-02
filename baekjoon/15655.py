# 백트래킹
# N과 M (6)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []


def dfs(idx):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(idx, n):
        result.append(lst[i])
        dfs(i+1)
        result.pop()


dfs(0)
