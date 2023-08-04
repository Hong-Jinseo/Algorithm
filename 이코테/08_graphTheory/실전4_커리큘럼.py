# 그래프 이론 (위상정렬)
# 커리큘럼
import copy
from collections import deque

n = int(input())

indegree = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]

    for j in temp[1:-1]:
        graph[j].append(i)
        indegree[i] += 1


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for r in result[1:]:
        print(r)


topology_sort()

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''