# 그리디
# 1이 될 때까지
# input 25 5 / output 2

n, k = map(int, input().split())
cnt = 0

while True:
    # k로 나눠지는 n에 가장 가까운 수 찾기 (0이 될
    temp = (n//k) * k
    cnt += n - temp
    n = temp

    # n을 k로 더 나눌 수 없다면 반복문 종료 ( n<k -> temp==0 )
    if n < k:
        break

    # k로 나누기
    n //= k
    cnt += 1

# (k로 더 나눌 수 없으니) 1이 될때까지 1씩 뺴기
cnt += n-1

print(cnt)