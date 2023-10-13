# 산타의 선물 공장 2
# https://www.codetree.ai/training-field/frequent-problems/problems/santa-gift-factory-2

import sys
input = sys.stdin.readline

MAX_N, MAX_M = 100000, 100000

# 노드 정보
pre, post = [0] * (MAX_M + 1), [0] * (MAX_M + 1)

# 벨트 정보
head, tail, length = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N


# 6. 벨트 정보 얻기
def get_belt_info(b_num):
    c = length[b_num]
    # 선물이 없는 벨트라면
    if c == 0:
        a, b = -1, -1
    else:
        a, b = head[b_num], tail[b_num]

    print(a + 2 * b + 3 * c)


# 5. 선물 정보 얻기
def get_present_info(p_num):
    a, b = pre[p_num], post[p_num]
    if a == 0:
        a = -1
    if b == 0:
        b = -1

    print(a + 2 * b)


# 4. 물건 나누기
def divide_stuff(src, dst):
    n = length[src] // 2

    if n == 0:
        print(length[dst])
        return

    first = last = head[src]
    for _ in range(n - 1):
        last = post[last]

    # src
    head[src] = post[last]
    pre[post[last]] = 0

    # dst
    if length[dst] == 0:
        tail[dst] = last
    post[last] = head[dst]
    pre[head[dst]] = last
    head[dst] = first
    pre[first] = 0

    # 개수 조정
    length[src] -= n
    length[dst] += n

    print(length[dst])


# head 삽입
def push_head(b_id, h_id):
    # 불가능한 경우
    if h_id == 0:
        return

    if length[b_id] == 0:
        head[b_id] = tail[b_id] = h_id
        pre[h_id] = post[h_id] = 0

    else:
        orig_head = head[b_id]

        head[b_id] = h_id
        pre[h_id], post[h_id] = 0, orig_head
        pre[orig_head] = h_id

    length[b_id] += 1


# head 삭제
def remove_head(b_id):
    # 불가능한 경우
    if length[b_id] == 0:
        return 0

    if length[b_id] == 1:
        deleted = head[b_id]
        head[b_id] = tail[b_id] = 0

    else:
        deleted = head[b_id]
        new_head = post[deleted]

        head[b_id] = new_head
        pre[new_head] = 0

    length[b_id] -= 1
    return deleted


# 3. 앞 물건만 교체하기
def switch_first_stuff(src, dst):
    src_head = remove_head(src)
    dst_head = remove_head(dst)

    push_head(dst, src_head)
    push_head(src, dst_head)

    print(length[dst])


# 2. 물건 모두 옮기기
def move_all_stuff(src, dst):
    # src에 물건이 없다면
    if length[src] == 0:
        print(length[dst])
        return

    # dst에 물건이 없다면 -> src가 dst가 됨
    if length[dst] == 0:
        head[dst], tail[dst] = head[src], tail[src]

    # 양쪽에 모두 물건이 있다면
    else:
        dst_head = head[dst]
        head[dst] = head[src]

        # src의 꼬리 -> dst의 머리
        src_tail = tail[src]
        post[src_tail] = dst_head
        pre[dst_head] = src_tail

    # SRC 초기화
    head[src] = tail[src] = 0

    # 길이 수정
    length[dst] += length[src]
    length[src] = 0

    print(length[dst])


# 1. 공장 설립
def build_factory(order):
    n, m = order[1], order[2]

    belts = [[] for _ in range(n + 1)]

    for i, line in enumerate(order[3:], start=1):
        belts[line].append(i)

    for i, belt in enumerate(belts):
        # 비어있는 벨트라면 pass
        if len(belt) == 0:
            continue

        # 벨트의 선물 수 기록
        length[i] = len(belt)

        # 첫 번째, 마지막 값 기록
        head[i] = belt[0]
        tail[i] = belt[-1]

        # 연속된 노드를 연결
        for j, present in enumerate(belt[:-1]):
            post[belt[j]] = belt[j + 1]
            pre[belt[j + 1]] = belt[j]


q = int(input())
for _ in range(q):
    order = list(map(int, input().split()))
    sign = order[0]

    # 1. 공장 설립
    if sign == 100:
        build_factory(order)

    # 2. 물건 모두 옮기기
    elif sign == 200:
        move_all_stuff(order[1], order[2])

    # 3. 앞 물건만 교체하기
    elif sign == 300:
        switch_first_stuff(order[1], order[2])

    # 4. 물건 나누기
    elif sign == 400:
        divide_stuff(order[1], order[2])

    # 5. 선물 정보 얻기
    elif sign == 500:
        get_present_info(order[1])

    # 6. 벨트 정보 얻기
    else:
        get_belt_info(order[1])
