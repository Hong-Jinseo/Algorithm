#백준 1431번
#시리얼 번호

def sum_number(input):
    result = 0

    for s in input:         # 문자열의 각 요소를 s에 대입
        if s.isdigit():     # s가 digit이라면 true 반환
            result += int(s)
            
    return result


N = int(input())
serial = [input() for _ in range(N)]    # 시리얼 넘버 저장하는 리스트

serial.sort(key= lambda x: (len(x), sum_number(x), x))
# serial의 각 요소를 길이, 자리수 합, 사전순으로 정렬

for i in serial:
    print(i)