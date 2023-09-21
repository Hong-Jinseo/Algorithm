# 완전탐색
# 전력망을 둘로 나누기

import copy
from collections import Counter


# 최상위 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 같은 부모로 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return parent


def solution(n, wires):
    answer = int(1e9)

    for i in range(len(wires)):

        # 부모 리스트 초기화
        parent = [0] * (n + 1)
        for j in range(1, n + 1):
            parent[j] = j

        # 끊고자 하는 전선 제외
        temp = copy.deepcopy(wires)
        temp.pop(i)

        # Union-find 연산 수행
        for s, e, in temp:
            parent = union_parent(parent, s, e)

        # 모든 값에 대해 find_parent 수행 (parent값 갱신하기 위함)
        for i in range(1, n + 1):
            find_parent(parent, i)

        # 두 전력망의 송전탑 차이 계산
        cnt = list(Counter(parent[1:]).items())
        answer = min(answer, abs(cnt[0][1] - cnt[1][1]))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# 3
