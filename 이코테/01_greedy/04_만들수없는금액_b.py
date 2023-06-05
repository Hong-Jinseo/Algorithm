# 그리디
# 만들 수 없는 금액
# 교재 이론설명 읽고 다시 풀었음

n = int(input())
coins = list(map(int, input().split()))

coins.sort()
target = 1       # 다음으로 만들어야 하는 수

for coin in coins:
    if coin <= target:
        target += coin
    else:
        break

print(target)