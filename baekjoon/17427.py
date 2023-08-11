# 수학
# 약수의 합 2

n = int(input())
total = 0
for i in range(1, n+1):
    # 약수의 합 += (n보다 작거나 같은 i의 배수의 개수) * i
    total += (n//i) * i

print(total)

'''
1 = 1
2 = 1 2
3 = 1   3
4 = 1 2   4
5 = 1       5
6 = 1 2 3     6
'''
