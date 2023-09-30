# 그리디
# 조이스틱

def solution(name):
    answer = 0
    n = len(name)
    A = ord('A')
    Z = ord('Z') + 1

    # [조이스틱 상하 이동]
    for i, alpha in enumerate(name):
        answer += min(ord(alpha) - A, Z - ord(alpha))

    # [조이스틱 좌우 이동]
    move = n - 1  # 최대값

    # 0부터 n-1까지 정방향으로 이동하는 모든 경우 탐색
    for forward in range(n):
        idx = forward + 1

        # '연속된 A' 찾기 (=정방향 이동의 마지막 시점)
        while idx < n and name[idx] == 'A':
            # '연속된 A'의 마지막 인덱스
            idx += 1

        # '연속된 A'의 가장 마지막 값에 역방향으로 접근하는 경우
        backward = n - idx

        move = min(move, forward * 2 + backward, forward + backward * 2)

    answer += move
    return answer
