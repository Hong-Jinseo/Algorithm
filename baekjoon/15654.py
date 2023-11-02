# 백트래킹
# N과 M (5)

import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

for temp in permutations(lst, m):
    print(' '.join(map(str, temp)))
