# 그리디
# 만들 수 없는 금액
from itertools import combinations as comb

n = int(input())
coins = list(map(int, input().split()))

coins.sort()
result = set()      # 모든 경우의 수가 들어있는 집합
result_num = 0               # 결과값


# 모든 경우의 수 구해서 정렬 -> 앞에서부터 없는 값 찾기
for i in range(1, n+1):
    temp = list(comb(coins, i))
    for j in temp:
        result.add(sum(j))

for k in range(1, sum(coins)):
    if k in result:
        continue
    else:
        result_num = k
        break

print(result_num)
