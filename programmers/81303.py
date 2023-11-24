# 표 편집

def up(num, exist):
    global now

    while num > 0:
        now -= 1
        if exist[now] == True:
            num -= 1


def down(num, exist):
    global now

    while num > 0:
        now += 1
        if exist[now] == True:
            num -= 1


# 삭제
def cross(exist, recent):
    # 삭제
    global now
    exist[now] = False
    recent.append(now)

    # 현위치 갱신 (마지막 값이 아니면)
    if True in exist[now:]:
        while not exist[now]:
            now += 1
    # (마지막 값이면)
    else:
        while not exist[now]:
            now -= 1


def back(exist, recent):
    temp = recent.pop()
    exist[temp] = True


def solution(n, k, cmd):
    answer = ''
    # U 위로, D 아래로, C 삭제 후 아래 행, Z 삭제행 복구

    # 연결리스트?
    global now
    now, recent = int(k), []

    exist = [True] * n

    for order in cmd:
        if len(order) > 2:
            order, num = order.split()

        if order == 'U':
            up(int(num), exist)
        elif order == 'D':
            down(int(num), exist)
        elif order == 'C':
            cross(exist, recent)
        else:
            back(exist, recent)

    for rst in exist:
        if rst:
            answer += 'O'
        else:
            answer += 'X'

    return answer
