# 그리디
# 숫자 카드 게임

# 아이디어 : 각 행에서 가장 숫자가 작은 카드의 값들 비교하기
n, m = map(int, input().split())
min_cards = []

for _ in range(n):
    cards = list(map(int, input().split()))
    min_cards.append(min(cards))

print(max(min_cards))