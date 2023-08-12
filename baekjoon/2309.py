# 부르트 포스
# 일곱 난쟁이

height = [int(input()) for _ in range(9)]
height.sort()

total = sum(height)

out = False
for i in range(8):
    for j in range(i, 9):
        if total - height[i] - height[j] == 100:
            height.pop(j)
            height.pop(i)
            out = True
            break
    if out:
        break

print('\n'.join(map(str, height)))
