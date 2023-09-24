# 백트래킹
# N과 M

n, m = map(int, input().split())
stack = []


def dfs(start):
    # 길이가 m이 되면
    if len(stack) == m:
        for i in range(m):
            print(stack[i], end=' ')
        return

    # 길이가 m이 아니면
    for i in range(start, n + 1):
        # i가 이미 처리된 값이면
        if i in stack:
            continue

        # i를 선택 -> dfs(i) -> i 해제
        stack.append(i)
        dfs(i)
        stack.pop()


dfs(1)
