# 그리디
# 설탕 배달

n = int(input())
answer = 0

while n >= 0:
    # 남은 설탕이 5의 배수라면 -> 5로 나누고 출력
    if n % 5 == 0:
        answer += n // 5
        print(answer)
        break

    # 3개의 설탕을 1개의 봉지에 담음
    n -= 3
    answer += 1
else:
    print(-1)
