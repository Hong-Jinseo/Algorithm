# 그래프 이론
# 최종 순위

from collections import deque


# 위상정렬
def topology_sort(v, ind, graphs):
    result = []
    q = deque()

    for i in range(1, v+1):
        if ind[i] == 0:
            q.append(i)

    for _ in range(v):
        # 큐가 비었다면 (= 사이클 발생)
        if len(q) == 0:
            return False
        # 큐의 원소개 2개 이상이라면 (= 가능한 정렬 결과가 여러 개)
        if len(q) >= 2:
            return False

        now = q.popleft()
        result.append(now)

        for i in graphs[now]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)

    return result


t = int(input())
rst = []

for _ in range(t):
    # input
    n = int(input())
    team = list(map(int, input().split()))  # team[i] : i등을 한 팀 번호
    m = int(input())

    indegree = [0] * (n + 1)
    graph = [[] for i in range(n + 1)]

    for i in range(n):
        for j in range(i+1, n):
            # 자기보다 낮은 등수를 원소로 갖는다
            graph[team[i]].append(team[j])
            indegree[team[j]] += 1

    impossible = False

    for _ in range(m):
        # a, b의 관계 역전
        a, b = map(int, input().split())

        if b in graph[a]:
            # b보다 a 등수가 낮은 경우 삭제
            graph[a].remove(b)
            indegree[b] -= 1
            # a보다 b 등수가 낮은 경우 추가
            graph[b].append(a)
            indegree[a] += 1

        else:
            # a보다 b 등수가 낮은 경우 삭제
            graph[b].remove(a)
            indegree[a] -= 1
            # b보다 a 등수가 낮은 경우 추가
            graph[a].append(b)
            indegree[b] += 1

    result = topology_sort(n, indegree, graph)

    if not result:
        rst.append("IMPOSSIBLE")
    else:
        rst.append(' '.join(map(str, result)))

for r in rst:
    print(r)
