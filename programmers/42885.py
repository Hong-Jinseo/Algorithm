# 그리디
# 구명보트

# 2차 풀이 (전과 동일)
def solution(people, limit):
    pair = 0
    h, t = 0, len(people) - 1  # 머리, 꼬리
    people.sort()

    while h < t:
        # 짝이 지어지면
        if people[h] + people[t] <= limit:
            pair += 1
            h += 1
            t -= 1

        # 짝이 지어지지 않으면 -> 무거운 사람 혼자 보트에 탑승
        else:
            t -= 1

    return len(people) - pair
