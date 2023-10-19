# 이분탐색
# 수 찾기

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for num in m_list:
    # n_list의 인덱스
    left, right = 0, n - 1
    found = False

    while left <= right:
        mid = (left + right) // 2

        if num == n_list[mid]:
            print(1)
            found = True
            break
        elif num < n_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if not found:
        print(0)

