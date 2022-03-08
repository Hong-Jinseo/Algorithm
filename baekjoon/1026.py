#백준 1026번
#보물

N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0

for _ in range(N):
    s += max(a_list) * min(b_list)  # a의 최댓값 * b의 최솟값
    a_list.remove(max(a_list))      # a에서 최댓값 삭제
    b_list.remove(min(b_list))      # b에서 최솟값 삭제

print(s)