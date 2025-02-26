# 힙
# 디스크 컨트롤러

import heapq

def solution(jobs):
    h = []
    answer = []
    sec = -1
    
    # 메인힙에 추가
    for idx, time in enumerate(jobs):
        req_time, spend_time = time
        heapq.heappush(h, (req_time, spend_time, idx))
    
    while h:
        sec += 1
        h2 = []

        # 후보힙에 후보 작업들 추가
        while h and h[0][0] <= sec:
            rt, st, i = heapq.heappop(h)
            heapq.heappush(h2, (st, rt, i))
        
        # 후보 작업이 있다면
        if h2:
            # 우선순위 높은 것 처리
            popped = heapq.heappop(h2)
            # print(popped, sec)
            sec += popped[0]    # 현재시간을 작업 끝난 시간으로 업데이트 (현재시간 += 소요시간)
            answer.append(sec - popped[1])  # 현재시간 - 요청시간
            print(sec, popped[1])

            # 남은 작업 다시 메인 힙으로
            h.extend([(y, x, z) for x, y, z in h2])
            heapq.heapify(h)

            # 시간 정정 (<- 이 과정에서 걸리는 시간은 없다고 가정합니다)
            sec -= 1

    print(answer)
    return sum(answer) // len(answer)

print(solution([[0, 3], [1, 9], [3, 5]]))
# 8