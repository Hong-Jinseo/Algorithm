# 정렬
# 카드 정렬하기

import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0

while len(cards) != 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    result += temp
    heapq.heappush(cards, temp)

print(result)
