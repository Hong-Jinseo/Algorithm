# 이진 탐색
# 고정점 찾기


def search(a):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == mid:
            return mid

        # 원소가 인덱스보다 크다면 -> 왼쪽 파트 탐색
        if a[mid] > mid:
            end = mid - 1
        # 원소가 인덱스보다 작다면 -> 오른쪽 파트 탐색
        else:
            start = mid + 1

    return -1


# 고정점 : 인덱스 == 원소
n = int(input())
lst = list(map(int, input().split()))

print(search(lst))

'''
5
-15 -6 1 3 7
# 3

7
-15 -4 2 8 9 13 15
# 2

7
-15 -4 3 8 9 13 15
# -1
'''