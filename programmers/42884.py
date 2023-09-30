# 그리디
# 단속카메라

# 2차 풀이
def solution(routes):
    answer = 0
    camera = int(-1e9)  # 카메라 위치

    # 진출시간 기준 오름차순 정렬
    routes.sort(key=lambda x: x[1])

    for i, o in routes:
        # 카메라 위치 < 신규 차량의 진입시간 (-> 이 경우, 신규 차량은 카메라에 잡히지 않음)
        if camera < i:
            camera = o  # 카메라의 위치를 신규차량의 진출시간으로 갱신
            answer += 1

    return answer

'''
# 1차 풀이
def solution(routes):
    answer = 0
    routes.sort()
    get_in, get_out = [], []  # 현재 도로 위에 있는 차들의 진입시간, 진출시간

    for i, o in routes:

        # 진출 기록
        get_out.append(o)
        get_out.sort()

        # 진입, 진출이 동시에 발생할 경우
        if get_out[0] == i:
            get_in, get_out = [], []  # 카메라 설치 -> 도로 위의 모든 차 단속
            answer += 1

        # 현재 도로 위의 차와 겹치는 범위가 없는 경우
        # (도로 위 차량의 가장 빠른 진출시간 < 새로운 차의 진입시간)
        elif get_out[0] < i:
            get_in, get_out = [i], [o]  # 카메라 설치 -> 방금 진입한 차 제외하고 단속
            answer += 1

        else:
            # 진입 기록
            get_in.append(i)

    # 도로에 남아있는 차량이 있다면 카메라 하나 더 설치
    if get_in:
        return answer + 1

    return answer
'''


print(solution([[-2, -1], [1, 2], [-3, 0]]))  # 2
print(solution([[0, 1], [2, 3], [4, 5], [6, 7]]))  # 4
print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[0, 0], ]))  # 1
print(solution([[0, 1], [0, 1], [1, 2]]))  # 1
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
print(solution([[-20, 15], [-20, -15], [-14, -5], [-18, -13], [-5, -3]]))  # 2
