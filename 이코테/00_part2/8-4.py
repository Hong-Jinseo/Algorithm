# 피보나치 (반복)

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
