# 구현
# 성적 통계

k = int(input())

for i in range(k):
    temp = list(map(int, input().split()))
    score = temp[1:]
    score.sort(reverse=True)

    compare = 0
    for j in range(temp[0]-1):
        compare = max(compare, score[j] - score[j+1])

    print('Class', i+1)
    print('Max '+str(score[0])+', Min '+str(score[-1]) + ', Largest gap '+str(compare))
