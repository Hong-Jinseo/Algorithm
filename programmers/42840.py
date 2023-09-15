# 완전탐색
# 모의고사

def solution(answers):
    answer = [0] * 3

    ans_p1 = [1, 2, 3, 4, 5]  # 5
    ans_p2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    ans_p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    for i in range(len(answers)):
        j1 = i % 5 if i > 4 else i
        j2 = i % 8 if i > 7 else i
        j3 = i % 10 if i > 9 else i

        if answers[i] == ans_p1[j1]:
            answer[0] += 1

        if answers[i] == ans_p2[j2]:
            answer[1] += 1

        if answers[i] == ans_p3[j3]:
            answer[2] += 1

    M = max(answer)
    member = []

    for i in range(3):
        if answer[i] == M:
            member.append(i + 1)

    return member


print(solution([1, 3, 2, 4, 2]))
# [1, 2, 3]
