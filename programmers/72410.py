# 구현
# 신규 아이디 추천

# 문자열 갱신
def update_id(user_id, index):
    return [value for i, value in enumerate(user_id) if index[i]]


# new_id의 모든 대문자를 대응되는 소문자로 치환
def step_01(user_id):
    for i, char in enumerate(user_id):
        if char.isupper():
            user_id[i] = user_id[i].lower()


# new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
def step_02(user_id, index):
    allowed = ['-', '_', '.']
    temp = []

    for i, char in enumerate(user_id):
        if not (48 <= ord(char) <= 57 or 97 <= ord(char) <= 122 or char in allowed):
            index[i] = False


# new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
def step_03(user_id, index):
    pre = ''

    for key, value in index.items():
        now = user_id[key]
        # 삭제되지 않은 값이고 + 현재 값이 마침표이고 + 앞의 값이 마침표라면 -> 삭제
        if value:
            if now == '.' and pre == '.':
                index[key] = False
            pre = now


# new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
def step_04(user_id):
    while user_id and user_id[-1] == '.':
        user_id.pop()

    i = 0
    while i < len(user_id) and user_id[i] == '.':
        i += 1

    return user_id[i:]


# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입
def step_05(user_id):
    if not user_id:
        user_id.append('a')


# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
def step_07(new_id):
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id.append(new_id[-1])


def solution(new_id):
    new_id = list(new_id)
    index = {i: True for i in range(len(new_id))}

    step_01(new_id)
    step_02(new_id, index)
    step_03(new_id, index)
    new_id = update_id(new_id, index)  # 문자열 갱신
    new_id = step_04(new_id)
    step_05(new_id)

    # 6단계: 문자열 길이 조정, 마지막의 마침표 삭제
    new_id = new_id[:15]
    new_id = step_04(new_id)
    step_07(new_id)

    return ''.join(new_id)
