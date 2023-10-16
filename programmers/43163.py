# BFS
# 단어 변환

# 2차 풀이
from collections import deque


def can_change(begin, target):
    cnt = 0
    for b, t in zip(begin, target):
        # 같은 순서의 알파벳이 서로 다르다면 cnt += 1
        if b != t:
            cnt += 1

    # 서로 다른 알파벳이 하나뿐이라면 True 반환
    return True if cnt == 1 else False


def solution(begin, target, words):
    n = len(words)

    used = [False] * n
    q = deque([(begin, 0)])

    while q:
        now, cnt = q.popleft()

        for i, word in enumerate(words):
            # 아직 사용하지 않았고 and 바꿀 수 있는 단어라면
            if not used[i] and can_change(now, word):

                # 그 단어가 타겟 단어라면
                if word == target:
                    return cnt + 1

                used[i] = True
                q.append((word, cnt + 1))

    return 0

'''
# 1차 풀이
from collections import deque


# a -> b 변환이 가능한지 체크
def check(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):

    q = deque([(begin, 0)])  # (단어, 단계)
    visited = [begin]

    while q:
        now, count = q.popleft()

        if now == target:
            return count

        for post in words:
            if check(now, post) and post not in visited:
                q.append((post, count + 1))
                visited.append(post)

    return 0
'''

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
