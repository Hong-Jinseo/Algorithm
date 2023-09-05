# 해시
# 베스트앨범


def solution(genres, plays):
    answer = []

    total_play = dict()     # 장르별 재생 횟수 합
    category = dict()       # 장르별 포함된 음악의 (재생수, 번호)

    for i in range(len(plays)):
        # 딕셔너리에 이미 저장된 장르라면
        if genres[i] in total_play:
            total_play[genres[i]] += plays[i]           # total_play[장르명]에 재생횟수 누적으로 더하기
            category[genres[i]].append((plays[i], i))   # category[장르명]의 리스트에 값 추가

        # 처음 나온 장르라면
        else:
            total_play[genres[i]] = plays[i]            # total_play[장르명] = 재생 횟수
            category[genres[i]] = [(plays[i], i)]       # category[장르명]에 튜플(재생수, 번호)을 담는 리스트 생성

    # 재생 횟수 기준으로 내림차순 정렬
    s = sorted(total_play.items(), key=lambda x: (-x[1]))

    # 재생 횟수가 큰 장르부터
    for i in range(len(s)):
        genre = s[i][0]     # 장르명
        category[genre].sort(key=lambda x: -x[0])   # 특정 장르의 노래를, 재생 횟수 내림차순 정렬

        # 상위 2개의 노래 번호만 리턴값에 추가
        temp = category[genre][0:2]
        for t in temp:
            answer.append(t[1])

    print(answer)
    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
