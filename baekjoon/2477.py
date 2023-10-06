# 구현
# 참외밭

k = int(input())
temp = [input().split() for _ in range(6)]
direction = [int(t[0]) for t in temp]
length = [int(t[1]) for t in temp]

large, small = [], []

for i in range(1, 5):
    # 방향이 한 번만 등장하면
    if direction.count(i) == 1:
        # 가장 긴 가로/세로 변을 의미함 (긴 변에 해당하는 길이 저장)
        idx = direction.index(i)
        large.append(length[idx])

        # 긴 변 + 3번의 입력 = 짧은 변
        idx = idx+3 if idx+3 < 6 else idx-3
        small.append(length[idx])

border = large[0] * large[1] - small[0] * small[1]
print(border * k)

