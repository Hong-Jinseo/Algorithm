# 정렬
# 실패율

def solution(N, stages):
    arrived = [0] * (N+2)   # 도달한 사람 수
    now = [0] * (N+2)       # 클리어 못한 사람 수 (플레이어들의 현위치)

    for s in stages:
        now[s] += 1
        for i in range(1, s+1):
            arrived[i] += 1

    rate = dict()           # 실패율을 저장하는 딕셔너리 (레벨: 실패율)
    for i in range(1, N+1):
        if arrived[i] == 0:
            rate[i] = 0
        else:
            rate[i] = now[i] / arrived[i]

    answer = sorted(rate, key=lambda x: -rate[x])
    return answer


# 프로그래머스에서는 print문 삭제 후 제출
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

