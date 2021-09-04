#입국심사

def solution(n, times):
    #시간초과 코드
    timeList = []
    times.sort()

    for i in range(1, n+1):
        for j in range(len(times)):
            timeList.append(i*times[j])

    timeList.sort()

    return timeList[n-1]


n = int(input())
times = list(map(int, input().split()))

print(solution(n, times))
