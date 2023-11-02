# 백트래킹
# N과 M (11)

from itertools import product

n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = set()

for temp in product(lst, repeat=m):
    answer.add(temp)

answer = sorted(list(answer))
for a in answer:
    print(' '.join(map(str, a)))
