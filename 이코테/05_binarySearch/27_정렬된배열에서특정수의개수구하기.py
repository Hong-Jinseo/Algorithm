# 이진탐색
# 정렬된 배열에서 특정 수의 개수 구하기

# 가장 작은 인덱스의 x
def binary_search_min(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        # mid가 target과 같다면 end 값을 감소시키며 가장 앞의 index에 접근
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


# 가장 큰 인덱스의 x
def binary_search_max(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        # mid가 target과 같다면 start 값을 증가시키며 가장 뒤의 index에 접근
        if array[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return end


n, x = map(int, input().split())
lst = list(map(int, input().split()))

left = binary_search_min(lst, x)
right = binary_search_max(lst, x)

result = right - left + 1
if result == 0:
    result = -1

print(result)
