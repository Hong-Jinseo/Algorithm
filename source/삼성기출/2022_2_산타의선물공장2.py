# 산타의 선물 공장 2
# https://www.codetree.ai/training-field/frequent-problems/problems/santa-gift-factory-2


import sys

input = sys.stdin.readline


# 벨트 정보 얻기
def belt_info(b_num):
    a, b, c = -1, -1, 0
    if belts[b_num]:
        a = belts[b_num][0]
        b = belts[b_num][-1]
        c = len(belts[b_num])

    print(a + 2 * b + 3 * c)


# 선물 정보 얻기
def stuff_info(p_num):
    for i, bt in enumerate(belts):
        for j, p in enumerate(bt):
            # 선물을 찾았다면
            if p == p_num:
                a = belts[i][j - 1] if j - 1 >= 0 else -1
                b = belts[i][j + 1] if j + 1 < len(belts[i]) else -1
                print(a + 2 * b)
                return


# 물건 나누기
def divide_stuff(m_src, m_dst):
    n = len(belts[m_src])

    if n == 1:
        print(len(belts[m_dst]))
        return

    n //= 2

    belts[m_dst] = belts[m_src][:n] + belts[m_dst]
    belts[m_src] = belts[m_src][n:]
    print(len(belts[m_dst]))


# 앞 물건만 교체하기
def switch_first_stuff(m_src, m_dst):
    # 두 벨트에 모두 선물이 있다면
    if belts[m_src] and belts[m_dst]:
        belts[m_src][0], belts[m_dst][0] = belts[m_dst][0], belts[m_src][0]

    # m_src 벨트에만 선물이 있다면
    elif belts[m_src]:
        # belts[m_dst] = deque([belts[m_src].popleft()])
        belts[m_dst] = [belts[m_src].pop(0)]

    # m_dst 벨트에만 선물이 있다면
    elif belts[m_dst]:
        # belts[m_src] = deque([belts[m_dst].popleft()])
        belts[m_src] = [belts[m_dst].pop(0)]

    print(len(belts[m_dst]))


# 물건 모두 옮기기
def move_all_stuff(m_src, m_dst):
    belts[m_dst] = belts[m_src] + belts[m_dst]
    belts[m_src] = []

    print(len(belts[m_dst]))


Q = int(input())

## 1. 공장 설립 ##
order = list(map(int, input().split()))
N, M = order[1], order[2]

# 벨트에 물건 얹기
# belts = [deque([]) for _ in range(N+1)]
belts = [[] for _ in range(N + 1)]
for idx, num in enumerate(order[3:], start=1):
    belts[num].append(idx)

for _ in range(Q - 1):
    order = list(map(int, input().split()))
    sign = order[0]

    # 물건 모두 옮기기
    if sign == 200:
        move_all_stuff(order[1], order[2])


    # 앞 물건만 교체하기
    elif sign == 300:
        switch_first_stuff(order[1], order[2])


    # 물건 나누기
    elif sign == 400:
        divide_stuff(order[1], order[2])


    # 선물 정보 얻기
    elif sign == 500:
        stuff_info(order[1])


    # 벨트 정보 얻기
    elif sign == 600:
        belt_info(order[1])