# 그리디
# 거스름돈
# input 1260, output 6

n = int(input())
coins = [500, 100, 50, 10]
cnt = 0

for c in coins:
    cnt += n//c
    n %= c

print(cnt)

# 시간복잡도 : O(K) (K는 화폐의 종류, 반복문이 화폐의 종류만큼 반복되기 때문)