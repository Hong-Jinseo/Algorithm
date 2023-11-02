# 백트래킹
# N과 M (12)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = set()
temp = []


def dfs(idx):
    if len(temp) == m:
        answer.add(tuple(temp))
        return

    for i in range(idx, n):
        temp.append(lst[i])
        dfs(i)
        temp.pop()


dfs(0)

for a in sorted(list(answer)):
    print(' '.join(map(str, a)))
