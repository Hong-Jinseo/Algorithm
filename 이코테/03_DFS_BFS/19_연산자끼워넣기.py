# DFS (깊이우선탐색)
# 연산자 끼워 넣기

n = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값
minimum = 1e9
maximum = -1e9


def dfs(cnt, now):
    global add, sub, mul, div, minimum, maximum

    # 연산을 n번 진행했다면 최솟값, 최댓값 재계산
    if cnt == n:
        minimum = min(now, minimum)
        maximum = max(now, maximum)
        return

    # 사용 가능한 연산자가 남았다면 계속해서 연산
    else:
        if add > 0:
            add -= 1
            dfs(cnt+1, now + array[cnt])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(cnt + 1, now - array[cnt])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(cnt + 1, now * array[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt + 1, int(now / array[cnt]))
            div += 1


dfs(1, array[0])

print(maximum)
print(minimum)