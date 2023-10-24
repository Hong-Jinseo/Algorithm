# 이분탐색
# 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

sorted_lst = sorted(list(set(lst)))

# i보다 작은 값의 개수 = 오름차순 정렬했을 때, i보다 앞에 있는 수의 개수 = 정렬시 i의 인덱스
sorted_dic = dict()
for i, value in enumerate(sorted_lst):
    sorted_dic[value] = i

print(' '.join(map(str, [sorted_dic[num] for num in lst])))
