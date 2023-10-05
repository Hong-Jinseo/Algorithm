# 구현
# 자물쇠와 열쇠

def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행
    m = len(a[0])  # 열

    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


def check(new_lock):
    lock_length = len(new_lock) // 3

    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠 크기 3배 늘리기
    # (lock 좌우에 key가 들어갈 공간인데, key는 lock보다 클 수 없음)
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 상하좌우
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        # 키 시작지점
        for x in range(n * 2):
            for y in range(n * 2):
                # 키 맞추기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 결과 검사
                if check(new_lock):
                    return True

                # 키 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False
