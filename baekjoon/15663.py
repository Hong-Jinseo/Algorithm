# 백트래킹
# N과 M (9)

from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = set()
for temp in permutations(lst, m):
    answer.add(temp)

answer = list(answer)

# 10~14 line 대신, 이런 코드도 가능함
# answer = list(set(permutations(lst, m)))
answer.sort()

for a in answer:
    print(' '.join(map(str, a)))
