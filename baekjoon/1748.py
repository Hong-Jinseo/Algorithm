# 브루트 포스
# 수 이어 쓰기 1

n = int(input())

digit = 1     # 자릿수
cnt = 9     # 숫자의 개수
answer = 0

while n > cnt:
    n -= cnt
    answer += cnt * digit

    digit += 1
    cnt *= 10

answer += n * digit

print(answer)

'''
한 자리 수 : 9개 (1~9)
두 자리 수 : 90개 (10~99)
세 자리 수 : 900개 (100~999)
네 자리 수 : 9000개 (1000~9999)
'''
