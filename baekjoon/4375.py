# 수학
# 1

while True:
    try:
        n = int(input())
    except:
        break

    i = '1'
    while int(i) % n != 0:
        i += '1'
    print(len(str(i)))
