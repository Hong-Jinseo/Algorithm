# 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 헤더부터 탐색해 뒤에 새로운 노드 추가
    def append(self, data):
        now = self.head
        while now.next is not None:
            now = now.next
        now.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):
        now = self.head
        while now is not None:
            print(now.data)
            now = now.next

    # 노드 인덱스 알아내기
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            node = node.next
            cnt += 1
        return node

    # 특정 위치에 노드 삽입
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # 앞뒤 노드 파악
        pre_node = self.get_node(index-1)
        post_node = pre_node.next

        # 새로운 노드 연결
        pre_node.next = new_node
        new_node.next = post_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next
