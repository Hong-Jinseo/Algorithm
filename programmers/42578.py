# 해시
# 의상

from collections import Counter

def solution(clothes):
    result = 1
    category = dict()
    
    # 카테고리 별 의상 개수 세기
    for n, c in clothes:
        if c in category:
            category[c] += 1
        else:
            category[c] = 1
    
    # 각 의상을 고르는 경우 + 아예 안 고르는 경우
    for key in category:
        result *= (category[key] + 1)
    
    # 모든 의상을 안 고르는 경우 제외
    return result - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

'''
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	3
'''