# 백트래킹
# N과 M (3)

from itertools import product

n, m = map(int, input().split())
lst = [str(i) for i in range(1, n+1)]

for temp in product(lst, repeat=m):
    for t in temp:
        print(t, end=' ')
    print()

