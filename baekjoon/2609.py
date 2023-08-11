# 수학
# 최대공약수와 최소공배수

num = list(map(int, input().split()))
temp = sorted(num)

# 유클리드 호제법
while temp[1] > 0:
    temp[0], temp[1] = temp[1], temp[0] % temp[1]

mi = temp[0]
ma = mi * (num[0] // mi) * (num[1] // mi)

print(mi)
print(ma)

