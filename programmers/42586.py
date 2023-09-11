# 스택/큐
# 기능개발

from collections import deque


def solution(progresses, speeds):
    answer = []

    fin = []
    lastest = 0

    index = [True for i in range(len(speeds))]

    while any(index):
        # 하루에 배포된 기능 수
        count = 0

        # 하루 작업 진도
        for i in range(len(speeds)):
            if index[i]:
                progresses[i] += speeds[i]
                if progresses[i] >= 100:
                    fin.append(i)
                    index[i] = False

        fin.sort(reverse=True)

        # 배포
        while fin and fin[-1] == lastest:
            fin.pop()
            lastest += 1
            count += 1

        if count > 0:
            answer.append(count)

    print(answer)
    return answer