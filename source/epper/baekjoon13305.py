# 주유소 최소비용

"""
[입력]
4
2 3 1
5 2 4 1

[출력]
18
"""

def solution(cities, distance, price):
    #처음 쓴 코드

    minCost = int(price[0])
    cost = 0

    for i in range(cities-1):
        if minCost > price[i]:
            minCost = price[i]
        cost += minCost * distance[i]
               
    return cost


cities = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

print(solution(cities, distance, price))

