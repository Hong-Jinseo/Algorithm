# 수학
# 시험 감독

n = int(input())
tester = list(map(int, input().split()))
a, b = map(int, input().split())

for i in tester:
    i -= a

    if i > 0:
        if i % b:
            n += (i//b) + 1
        else:
            n += i//b

print(n)
