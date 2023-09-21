# 그리디
# 체육복

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


print(solution(5, [2, 4], [1, 3, 5]))
# 5
