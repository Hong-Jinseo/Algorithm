# 완전탐색
# 소수 찾기

from itertools import permutations


def prime_number(num):
    if num <= 1:
        return [False, False]

    array = [True] * (num + 1)
    array[0] = False
    array[1] = False

    for i in range(2, num + 1):
        # num이 소수일 때
        if array[i] == True:
            j = 2
            # num의 배수는 소수가 아님
            while i * j <= num:
                array[i * j] = False
                j += 1

    return array


def solution(numbers):
    answer = set()
    numbers = list(numbers)

    # 숫자 만들기
    for i in range(1, len(numbers) + 1):
        nPr = list(permutations(numbers, i))
        for j in nPr:
            a = ''.join(j)
            answer.add(int(a))

    answer = list(answer)
    answer.sort()

    # 소수 찾기
    prime = prime_number(answer[-1])
    count = 0

    for a in answer:
        if prime[a]:
            count += 1
            print(a)

    return count