# 부르트 포스
# 날짜 계산

# 지구 15, 태양 28, 달 19
e, s, m = map(int, input().split())

i = 1
while True:
    # 올해
    #   = 15의 배수 + e
    #   = 28의 배수 + s
    #   = 19의 배수 + m

    if (i-e) % 15 == 0 and (i-s) % 28 == 0 and (i-m) % 19 == 0:
        break
    i += 1

print(i)

