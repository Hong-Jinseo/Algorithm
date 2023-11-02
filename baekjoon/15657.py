# 백트래킹
# N과 M (8)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []     # 오름차순


def dfs(idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(idx, n):
        answer.append(lst[i])
        dfs(i)
        answer.pop()

dfs(0)
