# 그리디 (크루스칼)
# 섬 연결하기


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return parent


def solution(n, costs):
    answer = 0
    p = [i for i in range(n + 1)]  # 부모

    # 비용 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    for start, end, cost in costs:
        # 사이클이 발생하지 않으면 (= 부모 노드가 다르면, 아직 연결된 노드가 아니라면)
        if find_parent(p, start) != find_parent(p, end):
            # 연결 & 비용 계산
            union_parent(p, start, end)
            answer += cost

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
# 4
