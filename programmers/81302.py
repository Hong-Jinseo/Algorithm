# 거리두기 확인하기


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def find_distance(graph, x, y):
    # 상하좌우 붙어있는 경우, 상하좌우 한 칸 떨어진 경우, 대각선
    dx = [1, -1, 0, 0, 2, -2, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 0, 0, 2, -2, 1, -1, 1, -1]

    for i in range(12):
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx, ny):
            # 상하좌우 붙어있는 경우
            if i < 4:
                if graph[nx][ny] == 'P':
                    return False

            # 상하좌우 한 칸 떨어진 경우
            elif 4 <= i < 8:
                if graph[nx][ny] == 'P':
                    # 중간에 파티션이 없다면 (빈자리라면)
                    mx, my = (x + nx) // 2, (y + ny) // 2
                    if graph[mx][my] == 'O':
                        return False

            # 대각선
            else:
                if graph[nx][ny] == 'P':
                    if graph[x][ny] == 'O' or graph[nx][y] == 'O':
                        return False
    return True


def solution(places):
    answer = []

    # P 응시자, O 빈자리, X 파티션
    for place in places:

        people = []  # 응시자 좌표
        done = False  # 결과값을 찾았는지 여부

        # 응시자 위치 기록
        for i, row in enumerate(place):
            for j, col in enumerate(row):
                if col == 'P':
                    people.append((i, j))

        # 각 응시자 기준 맨해튼 거리 2 이내에 다른 응시자가 있다면
        for x, y in people:
            if not find_distance(place, x, y):
                answer.append(0)
                done = True
                break

        # 모든 응시자 간 맨해튼 거리가 2 초과인 경우
        if not done:
            answer.append(1)

    return answer
