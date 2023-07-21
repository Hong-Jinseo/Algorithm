## 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i   # 가장 작은 원소의 인덱스

    # 정렬되지 않은 원소에 순차적으로 접근
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프 연산

print(array)



## 삽입 정렬

array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array2)):
    for j in range(i, 0, -1):
        if array2[j] < array2[j-1]: # 한 칸씩 왼쪽으로 이동
            array2[j], array2[j-1] = array2[j-1], array2[j]
        else:   # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array2)



## 퀵 정렬

array3 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(start, end):
    # 원소개 1개인 경우 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array3[left] <= array3[pivot]:
            left += 1
        while right > start and array3[right] >= array3[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array3[pivot], array3[right] = array3[right], array3[pivot]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array3[left], array3[right] = array3[right], array3[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(start, right-1)
    quick_sort(right+1, end)


quick_sort(0, len(array3)-1)
print(array3)



## 계수 정렬

# 모든 원소의 값이 0보다 크거나 같다고 가정
array4 = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array4) + 1)

for i in range(len(array4)):
    count[array4[i]] += 1        # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):     # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')       # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력






