# 그리디
# AB

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = ['B'] * n


def count(data):
    cnt = 0
    for i in range(n-1):
        if data[i] == 'A':
            # A 뒤에 나오는 값이 B라면 cnt += 1
            for j in range(i+1, n):
                if data[j] == 'B':
                    cnt += 1
    return cnt


# s의 앞에서부터 하나씩 A로 변경
for i in range(n):
    s[i] = 'A'

    # s가 문제의 조건을 만족한다면
    if count(s) == k:
        print(''.join(s))
        exit(0)

    # s가 문제의 조건을 초과했다면
    if count(s) > k:
        # A 원상복구
        s[i] = 'B'

print(-1)
