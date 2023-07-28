# 이진탐색
# 가사 검색

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def search_word(a, target):
    cnt = target.count('?')

    if cnt == len(target):
        return len(a)

    left = target.replace('?', 'a')
    right = target.replace('?', 'z')

    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)

    return right_index - left_index


def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    words.sort(key=lambda x: (len(x), x))

    for w in words:
        array[len(w)].append(w)
        reversed_array[len(w)].append(w[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        len_q = len(query)

        if query[-1] == '?':
            answer.append(search_word(array[len_q], query))
        else:
            answer.append(search_word(reversed_array[len_q], query[::-1]))

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
