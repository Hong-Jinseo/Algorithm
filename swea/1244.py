# 백트래킹
# 최대 상금

def dfs(start, count):
    global result

    # 교환 횟수를 채웠다면 -> 반환
    if count == int(cnt):
        result = max(int(''.join(numbers)), result)
        return

    # 교환 시작
    for now in range(start, len(numbers)):
        for max_idx in range(now+1, len(numbers)):
            if numbers[now] <= numbers[max_idx]:
                numbers[now], numbers[max_idx] = numbers[max_idx], numbers[now]
                dfs(now, count+1)
                numbers[max_idx], numbers[now] = numbers[now], numbers[max_idx]

    # 이미 내림차순 정렬된 경우였다면 (앞 교환에서 아무 변화가 없었다면)
    if result == 0 and count < int(cnt):
        # 홀수라면 가장 마지막 수 2개 변경
        if (int(cnt) - count) % 2 == 1:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        dfs(start, int(cnt))


T = int(input())
for tc in range(1, T + 1):
    # 숫자판의 정보, 교환 횟수
    numbers, cnt = input().split()
    numbers = list(numbers)
    result = 0

    dfs(0, 0)
    print('#%d %d' % (tc, result))
