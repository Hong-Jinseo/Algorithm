# DP
# 퇴사

n = int(input())
graph = []
for _ in range(n):
    # 상담 시간, 금액
    t, p = map(int, input().split())
    graph.append((t, p))

d = [0] * (n+1)     # 누적 금액 (1~n)

# 기준 일자 i
for i in range(n):
    # 기준 일자에 상담을 할 경우, 상담이 끝나는 날부터 마지막 날까지 j
    for j in range(i+graph[i][0], n+1):
        # j일차 = max(i일차에 상담을 안 했을 경우, i일차에 상담을 해서 비용을 합산한 경우)
        d[j] = max(d[j], d[i]+graph[i][1])

print(d[n])
