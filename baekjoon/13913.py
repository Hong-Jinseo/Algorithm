# BFS
# 숨바꼭질 4

# DFS : 인접 노드의 인접 노드를 계속해서 탐색
# BFS : 인접 노드를 계속 큐에 넣어가며 큐에 들어온 순서대로 탐색

from collections import deque
MAX = 100000

n, k = map(int, input().split())

q = deque([(n, 0)])     # now, cnt
route = [0 for _ in range(MAX+1)]      # route[node] = node에 방문하기 직전에 방문한 노드

visited = [False] * (MAX+1)
visited[n] = True
cnt = 0


def find_route(node):
    result = [node]
    while node != n:
        node = route[node]
        result.append(node)

    result.reverse()
    print(' '.join(map(str, result)))


while q:
    now, cnt = q.popleft()

    if now == k:
        print(cnt)
        find_route(now)
        break

    for next_ in (now+1, now-1, now*2):
        if 0 <= next_ <= MAX and not visited[next_]:
            q.append((next_, cnt+1))
            visited[next_] = True
            route[next_] = now
