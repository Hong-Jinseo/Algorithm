# 백트래킹
# N과 M (10)

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
        dfs(i+1)
        temp.pop()


dfs(0)

answer = sorted(list(answer))

for a in answer:
    print(' '.join(map(str, a)))
