# 그리디
# 체육복

# 2차 풀이
def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    reserve = set(reserve)

    # 도난당했는데 여유분이 있던 사람 제외 (대칭차집합)
    temp = lost ^ reserve

    # 여전히 체육복이 필요한 사람, 여전히 체육복을 빌려줄 수 있는 사람 계산
    need = list(temp - reserve)
    need.sort()

    extra = [False] * (n + 1)
    for i in list(temp - lost):
        extra[i] = True

    # 빌려주기 수행
    for lt in need:
        # 앞 사람에게 빌리기
        if 0 < lt - 1 <= n and extra[lt - 1]:
            extra[lt - 1] = False

        # 뒷 사람에게 빌기기
        elif 0 < lt + 1 <= n and extra[lt + 1]:
            extra[lt + 1] = False

        # 빌리지 못한 사람
        else:
            answer += 1

    return n - answer


'''
# 1차 풀이
from collections import Counter


def solution(n, lost, reserve):
    answer = 0
    student = [True] * (n + 1)
    extra = [True] * (n + 1)

    lost.sort()
    reserve.sort()

    # 도난당한 학생 기록
    for i in lost:
        student[i] = False

    # 도난 + 여유분 -> 본인이 여유분을 사용함
    both = Counter(lost + reserve).most_common()
    for num, cnt in both:
        if cnt == 2:
            student[num] = True
            reserve.remove(num)
        else:
            break

    # 여분의 체육복을 가져온 학생
    for r in reserve:
        if extra[r]:
            # 앞 번호가 도난당했을 경우
            if 0 < r - 1 <= n and not student[r - 1]:
                student[r - 1] = True

            # 뒷 번호가 도난당했을 경우
            elif 0 < r + 1 <= n and not student[r + 1]:
                student[r + 1] = True

    return sum(student[1:])
'''

print(solution(5, [2, 4], [1, 3, 5]))
# 5
