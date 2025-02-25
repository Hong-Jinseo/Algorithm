# 큐
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    bridge_sum = 0  # sum(bridge) 사용할 경우 시간초과 발생하여 bridge_sum 변수 사용
    truck_weights = deque(truck_weights)
    answer = 0

    # 대기 트럭이 있으면
    while truck_weights:
        answer += 1
        bridge_sum -= bridge.popleft()

        # 현재 하중 + 신규 트럭 <= 최대 무게
        if bridge_sum + truck_weights[0] <= weight:
            new = truck_weights.popleft()
            bridge.append(new)
            bridge_sum += new
        else:
            bridge.append(0)
    
    # 다리 위에 남아있는 트럭
    answer += len(bridge)
    
    return answer

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# 110
