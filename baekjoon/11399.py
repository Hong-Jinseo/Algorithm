# 그리디
# ATM

n = int(input())
time = list(map(int, input().split()))
time.sort(reverse=True)

answer = 0
for i in range(n):
    answer += time[i] * (i+1)

print(answer)
