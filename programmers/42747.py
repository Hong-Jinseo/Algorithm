# 정렬
# H-Index

def solution(citations):
    h = len(citations)
    citations.sort(reverse=True)

    cnt = 0
    while h >= 0:
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
                if cnt >= h:
                    return h
        h -= 1

    return -1


# -- 다른 풀이 -- #


def solution2(citations):
    citations.sort()  # 오름차순 정렬

    for h in range(len(citations), -1, -1):
        if citations[-h] >= h:
            return h

    '''
    "h번 이상 인용된 논문"이 h편 이상이다
    = "h번 이상 인용된 논문 h편" 중 "가장 적게 인용된 논문의 인용 횟수"는 h 이상이다

    =>  "h번 이상 인용된 논문 h편"을 가정하고, 
        "가장 적게 인용된 논문의 인용 횟수"가 h 이상인지 확인한다

    ex)
    [3, 0, 6, 1, 5].sort() => [0, 1, 3, 5, 6]

    "0~4번 논문" 중 "0번 논문의 인용 횟수"가 5 이상인가? False
    "1~4번 논문" 중 "1번 논문의 인용 횟수"가 4 이상인가? False
    "2~4번 논문" 중 "2번 논문의 인용 횟수"가 3 이상인가? True -> return 3
    '''
