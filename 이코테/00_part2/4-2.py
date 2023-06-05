# 구현
# 시각

n = int(input())
cnt = 0

for i in range(n + 1):  # 0시부터 n시까지
    for j in range(60):  # 0분부터 59분까지
        for k in range(60):  # 0초부터 59초까지
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
