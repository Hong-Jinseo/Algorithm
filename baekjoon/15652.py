# 백트래킹
# N과 M (4)

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
answer = []


def dfs(start):
    # m개를 골랐다면
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n+1):
        answer.append(i)
        dfs(i)
        answer.pop()

dfs(1)
