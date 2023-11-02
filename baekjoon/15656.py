# 백트래킹
# N과 M (7)

from itertools import product

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for temp in product(lst, repeat=m):
    print(' '.join(map(str, list(temp))))
