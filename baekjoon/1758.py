#백준 1758번
#알바생 강호

N = int(input())
total = 0       #강호가 받을 수 있는 팁의 최댓값

tip = [int(input()) for _ in range(N)]  #팁 저장 리스트
tip.sort(reverse=True)      #팁 내림차순 정렬

for j in range(N):
    if (tip[j]-j > 0):      # tip[j] - ((j+1) - 1))              
        total += tip[j]-j

print(total)