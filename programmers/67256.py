# 키패드 누르기

def solution(numbers, hand):
    answer = ''

    # 키패드 좌표 입력 (graph[i번 버튼] = [x좌표, y좌표])
    number = 1
    graph = dict()
    for i in range(3):
        for j in range(3):
            graph[number] = [i, j]
            number += 1
    graph[0] = [3, 1]

    # 왼손, 오른손의 좌표 (*, #으로 초기화)
    loca_L, loca_R = [3, 0], [3, 2]

    for num in numbers:
        # 왼손 (1, 4, 7)
        if num % 3 == 1:
            loca_L = graph[num]
            answer += 'L'

        # 오른손 (3, 6, 9)
        elif num > 0 and num % 3 == 0:
            loca_R = graph[num]
            answer += 'R'

        # 비교
        else:
            x, y = graph[num]
            gap_L = abs(loca_L[0] - x) + abs(loca_L[1] - y)
            gap_R = abs(loca_R[0] - x) + abs(loca_R[1] - y)

            # 왼손이 더 가깝거나 or 거리가 같은데 왼손잡이면
            if gap_L < gap_R or (gap_L == gap_R and hand == 'left'):
                loca_L = graph[num]
                answer += 'L'
            # 오른손이 더 가깝거나 or 거리가 같은데 오른손잡이면
            else:
                loca_R = graph[num]
                answer += 'R'

    return answer
