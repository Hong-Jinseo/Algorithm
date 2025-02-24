# 해시
# 전화번호 목록


def solution(phone_book):
    phone_book.sort()

    for i, value in enumerate(phone_book[:-1]):
        # 사전순으로 정렬하면 인접한 케이스만 고려하면 됨
        if value == phone_book[i+1][:len(value)]:
            return False
    return True
    

'''
# 시간초과 코드
def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    
    for i, value in enumerate(phone_book):
        for j in range(i+1, len(phone_book)):
            if value == phone_book[j][:len(value)]:
                return False
    return True
'''


print(solution(["12","123","1235","567","88"]))

'''
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''