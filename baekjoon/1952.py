# 구현
# 달팽이 2

m, n = map(int, input().split())
answer = 0

x = m - 1
y = n

while True:
    # 가로 이동
    y -= 1
    answer += 1
    if y == 0:
        break

    # 세로 이동
    x -= 1
    answer += 1
    if x == 0:
        break

print(answer)
