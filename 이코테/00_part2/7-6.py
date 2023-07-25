# 이진탐색
# 부품 찾기

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))


def binary_search(lst, start, end, target):
    if end < start:
        return None
    mid = (start + end) // 2

    if lst[mid] == target:
        return mid

    elif lst[mid] > target:
        return binary_search(n_list, start, mid - 1, target)
    else:
        return binary_search(n_list, mid + 1, end, target)


for find in m_list:
    temp = binary_search(n_list, 0, n - 1, find)
    if temp is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
