# 그리디
# 모험가 길드

n = int(input())
fear = list(map(int, input().split()))
# 현재 그룹의 인원수, 구성된 모험가 그룹 수
current, total = 1, 0

fear.sort()
for i in range(n):
    if current >= fear[i]:
        total += 1
        current = 1
    else:
        current += 1

print(total)


