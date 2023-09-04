# 해시
# 전화번호 목록

def solution(phone_book):
    # 딕셔너리에 phone_book 값 저장
    dic = dict()
    for num in phone_book:
        dic[num] = True

    for num in phone_book:
        # 전화번호의 앞부분이 이미 있는 번호라면(=dic에 있다면)
        for i in range(1, len(num)):
            if num[0:i] in dic:
                return False
    return True


print(solution(["123","456","789"]))

'''
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
'''