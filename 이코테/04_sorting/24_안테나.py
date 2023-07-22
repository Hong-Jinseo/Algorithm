# 정렬
# 안테나

import statistics as st

n = int(input())
dist = list(map(int, input().split()))

dist.sort()
print(dist[(n-1)//2])
