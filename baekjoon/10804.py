#백준 10804
#카드 역배치

N = 10 #주어진 구간의 개수
card = [i for i in range(1, 21)] #1번부터 20번까지 카드 리스트에 저장

for _ in range(N):
    a, b = map(int, input().split())
    temp = card[a-1:b] #역배치 할 영역의 카드 번호 받아오기
    card[a-1:b] = temp[::-1] #역배치 후 기존 카드 리스트에 넣기

for i in card:
    print(i, end=' ') #' '로 출력 값들 이어주기