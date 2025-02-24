# 해시
# 베스트앨범

from collections import Counter

def solution(genres, plays):
    result = []
    lst = []
    cnt = dict()
    for i in range(len(genres)):
        lst.append([i, genres[i], plays[i]])
        # 장르 재생 총합 연산
        if genres[i] in cnt:
            cnt[genres[i]] += plays[i]
        else:
            cnt[genres[i]] = plays[i]
        
    # 장르 재생 총합(내림), 재생 수(내림), 고유번호(올림)
    lst.sort(key=lambda x: [-cnt[x[1]], -x[2], x[0]])
    
    # 각 장르당 2곡 제한
    genres_cnt = dict()
    for l in lst:
        num, gen = l[0], l[1]
        if gen not in genres_cnt:
            genres_cnt[gen] = 1
            result.append(num)
        elif genres_cnt[gen] < 2:
            genres_cnt[gen] += 1
            result.append(num)
        else:
            # 해당 else문 생략해도 됨
            genres_cnt[gen] += 1

    return result

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # [4, 1, 3, 0]
