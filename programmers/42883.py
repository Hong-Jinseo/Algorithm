# 그리디
# 큰 수 만들기

# 2차 풀이
def solution(number, k):
    out = 0
    stack = [number[0]]

    for i in range(1, len(number)):
        # 제거한 숫자가 k개가 되면 -> 제거 종료
        if out >= k:
            stack += number[i:]
            break

        now = number[i]

        # 높은 자릿수 >= 낮은 자릿수
        if stack[-1] >= now:
            stack.append(now)

        else:
            # 높은 자릿수 < 낮은 자릿수 and 제거한 숫자가 k개 미만이면
            while stack and stack[-1] < now and out < k:
                stack.pop()
                out += 1
            # 기존의 높은 자릿수 삭제 & 더 큰 수로 대체
            stack.append(now)

    # k만큼 제거되지 않았다면
    if k != out:
        # 가장 작은 숫자(=가장 낮은 자릿수에 위치함) 삭제
        stack = stack[:-(k - out)]

    return ''.join(stack)

'''
# 1차 풀이
def solution(number, k):
    stack = []  # 가장 큰 숫자를 저장할 스택

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    return ''.join(stack[:len(stack) - k])
'''
