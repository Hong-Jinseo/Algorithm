# 브루트 포스
# 카잉 달력

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    found = False
    while x <= m * n:
        if x % n == y % n:
            print(x)
            found = True
            break
        x += m

    if not found:
        print(-1)
