# 그리디
# 구명보트

def solution(people, limit):
    n = len(people)
    people.sort()

    i, j = 0, n - 1
    pair = 0

    while i < j:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            pair += 1
        else:
            j -= 1

    return n - pair
