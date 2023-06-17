# 구현
# 문자열 압축
from collections import deque


def solution(s):
    answer = len(s)

    # 문자열 단위를 1부터 len(s)까지 설정
    for i in range(1, len(s)+1):
        length = 0
        queue = deque(list(s))
        units = deque()
        data, result = "", 0

        # 단위로 분해
        while queue:
            for _ in range(i):
                if queue:
                    data += queue.popleft()
            units.append(data)
            data = ""

        # units의 첫 번째 값
        pre = units.popleft()
        final = ""

        if units:
            cnt = 1
        # units에 남은 값이 없으면 (단위가 len(s)면)
        else:
            cnt = 0
            length = i

        while units:
            post = units.popleft()
            # 패턴이 반복되면
            if pre == post:
                cnt += 1

            # 반복되지 않으면
            else:
                if cnt == 1:
                    length += i
                    final += post
                else:
                    length += len(str(cnt)) + i
                    final += str(cnt) + pre
                    cnt = 1

                # 만약 마지막 남은 문자열이라면
                if len(post) < i:
                    length += len(post)
                    final += str(cnt) + pre
                    cnt = 0
                    break

                pre = post

        if cnt == 1:
            length += i
            final += pre

        elif cnt > 1:
            length += len(str(cnt)) + i
            final += str(cnt) + pre

        answer = min(answer, length)

    # print(final)
    return answer


print(solution(input()))
