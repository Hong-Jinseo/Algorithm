# 정렬
# K번째수

def solution(array, commands):
    answer = []

    for i, j, k in commands:
        arr = array[i - 1:j]
        arr.sort()
        answer.append(arr[k - 1])

    print(answer)
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
# [5, 6, 3]
