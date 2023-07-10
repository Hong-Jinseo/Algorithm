
def solution(arr):
    result = []
    count = dict()

    for data in arr:
        if data not in count:
            count[data] = 1
        else:
            count[data] += 1

    for key in count:
        if count[key] > 1:
            result.append(count[key])

    if len(result) == 0:
        result.append(-1)

    return result


array = list(map(int, input().split()))
print(solution(array))
