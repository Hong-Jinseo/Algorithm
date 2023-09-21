# 완전탐색
# 모음사전

from itertools import product


def solution(word):
    answer = 0
    lst = ['A', 'E', 'I', 'O', 'U']

    dic = []
    for i in range(1, 6):
        for npr in product(lst, repeat=i):
            dic.append(''.join(npr))

    dic.sort()
    answer = dic.index(word)

    return answer + 1


print(solution("AAAAE"))
# 6
