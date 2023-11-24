# 표 편집

# 연결 리스트로 구현 (시간초과)
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 새로운 노드 추가
    def append(self, data):
        now = self.head
        while now.next is not None:
            now = now.next
        now.next = Node(data)
        now.next.prev = now

    # 길이 반환
    def length(self):
        cnt = 0
        now = self.head
        while now is not None:
            cnt += 1
            now = now.next
        return cnt

    # 모든 노드 값 출력
    def print_all(self):
        temp = []
        now = self.head
        while now is not None:
            # print(now.data, end=' ')
            temp.append(now.data)
            now = now.next
        return temp

    # 인덱스로 값 알아내기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            node = node.next
            cnt += 1
        return node

    # 삭제
    def delete_node(self, index):
        temp = None

        if index == 0:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

        node = self.get_node(index - 1)
        temp = node.next.data
        node.next = node.next.next
        if node.next is not None:
            node.next.prev = node

        return temp

    # 복구
    def add_node(self, value):
        new_node = Node(value)
        now = self.head

        # 첫 번째 자리로 복구되면
        if value < now.data:
            new_node.next = now
            now.prev = new_node
            self.head = new_node
            return

        while now.next is not None and now.next.data < value:
            now = now.next

        # 앞뒤 노드 파악
        prev_node = now
        post_node = now.next

        # 새로운 노드 연결
        prev_node.next = new_node
        new_node.prev = prev_node

        if post_node is not None:
            new_node.next = post_node
            post_node_prev = new_node


def solution(n, k, cmd):
    answer = ''
    # U 위로, D 아래로, C 삭제 후 아래 행, Z 삭제행 복구
    now, deleted = int(k), []

    # 연결리스트 생성
    llist = LinkedList(0)
    for i in range(1, n):
        llist.append(i)

    for order in cmd:
        if len(order) > 2:
            order, num = order.split()

        if order == 'U':
            now -= int(num)

        elif order == 'D':
            now += int(num)

        elif order == 'C':
            deleted.append(llist.delete_node(now))

            if llist.length() == now:
                now -= 1
        else:
            temp = llist.get_node(now).data  # 현재 선택된 값
            value = deleted.pop()  # 복구될 값
            llist.add_node(value)

            if value < temp:
                now += 1

    result = llist.print_all()

    for i in range(n):
        if i in result:
            answer += 'O'
        else:
            answer += 'X'

    return answer
