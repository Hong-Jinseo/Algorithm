# 스택/큐
# 기능개발

from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()

    for p, s in zip(progresses, speeds):
        q.append([p, s])
    
    while q:
        for i in range(len(q)):
            q[i][0] += q[i][1]  # 작업 진행
        
        cnt = 0
        while q and q[0][0] >= 100:
            q.popleft()
            cnt += 1
        
        if cnt > 0:
            answer.append(cnt)

    return answer


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
'''
progresses, speeds	return
[93, 30, 55], [1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''