# BFS
# 단어 변환

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


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
