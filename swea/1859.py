# 백만 장자 프로젝트

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    cost = list(map(int, input().split()))

    start, end, answer = -1, -1, 0

    while start < n-1:

        maximum = 0
        for i in range(end+1, n):
            if cost[i] > maximum:
                maximum = cost[i]
                end = i

        for j in range(start+1, end):
            answer += (maximum - cost[j])
        start = end

    print('#%d %d' % (tc, answer))
