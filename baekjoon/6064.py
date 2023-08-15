# 브루트 포스
# 카잉 달력

t = int(input())
answer = []

for _ in range(t):
    m, n, x, y = map(int, input().split())

    found = False
    while x <= m * n:
        if abs(x - y) % n == 0:
            print(x)
            found = True
            break
        x += m      # m을 더해도 카잉달력 기준으로 x값은 동일함

    if not found:
        print(-1)
