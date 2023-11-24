# 표 편집

# 연결리스트를 딕셔너리로 구현
def solution(n, k, cmd):
    answer = ['O'] * n
    now, deleted = int(k), []

    # 연결 리스트
    graph = {i: [i - 1, i + 1] for i in range(n)}  # graph[i] = [앞 노드, 뒷 노드]
    graph[0][0], graph[n - 1][1] = None, None  # head, tail은 None으로 설정

    # 명령어
    for order in cmd:
        if len(order) > 2:
            order, num = order.split()
            num = int(num)

        # 위로
        if order == 'U':
            for _ in range(num):
                now = graph[now][0]

        # 아래로
        elif order == 'D':
            for _ in range(num):
                now = graph[now][1]

        # 삭제
        elif order == 'C':
            answer[now] = 'X'

            # 삭제할 노드 기록
            prev, post = graph[now]
            deleted.append((prev, post, now))

            # 마지막 행이라면 바로 윗 행을, 아니라면 바로 아래 행을 선택
            now = graph[now][0] if post == None else graph[now][1]

            # 첫 번째 행이라면
            if prev == None:
                graph[post][0] = None

            # 마지막 행이라면
            elif post == None:
                graph[prev][1] = None

            else:
                graph[prev][1] = post
                graph[post][0] = prev

        # 복구
        else:
            prev, post, value = deleted.pop()
            answer[value] = 'O'

            if prev == None:
                graph[post][0] = value

            elif post == None:
                graph[prev][1] = value

            else:
                graph[post][0] = value
                graph[prev][1] = value

    return ''.join(answer)
