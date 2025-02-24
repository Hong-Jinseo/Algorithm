# 큐
# 같은 숫자는 싫어

def solution(arr):
    prev = arr[0]
    answer = [prev]

    # 원소가 하나일 경우
    if len(arr) == 1:
        return arr

    for num in arr[1:]:
        if num == prev:
            # 해당 if문 생략하고 !=만 써도 됨
            continue
        else:
            answer.append(num)
            prev = num

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
# [1, 3, 0, 1]
