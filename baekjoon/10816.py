# 이분탐색 (대신 counter 사용)
# 숫자 카드 2

from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

dic = dict(Counter(cards))

for t in target:
    if t in dic:
        print(dic[t], end=' ')
    else:
        print(0, end=' ')
