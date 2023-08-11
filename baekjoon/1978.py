# 수학
# 소수 찾기

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
cnt = 0

if lst[0] == 1:
    n -= 1

for num in lst:
    for i in range(2, num):
        # 1, i가 아닌 다른 수로 나눌 수 있으면 -> 소수 아님
        if num % i == 0:
            n -= 1
            break

print(n)
