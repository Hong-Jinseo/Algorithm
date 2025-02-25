# 큐
# 프로세스

from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0

    while q:
        target = q.popleft()
        location -= 1   # 타겟 프로세스 위치

        if not q:
            return answer + 1   # 이 경우도 pop되는 케이스이니 +1
        
        elif target < max(q):
            q.append(target)    # 다시 큐에 추가되는 경우, answer+=1 X
            if location == -1:
                location = len(q) - 1

        else:
            answer += 1         # pop 될 경우에만 +1 해줌
            if location == -1:
                return answer
            
    return answer
    

print(solution([1, 1, 9, 1, 1, 1], 0))
# 5

'''
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
'''