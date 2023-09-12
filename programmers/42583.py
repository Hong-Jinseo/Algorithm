# 큐
# 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    second = 0

    while truck_weights:

        passed = bridge.popleft()
        current_weight -= passed

        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)

        second += 1

    return second + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
# 8
