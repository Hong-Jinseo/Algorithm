#백준 1758번
#알바생 강호

N = int(input())
tip = []        #N개 줄의 각 사람이 주려고 하는 팁
total = 0       #강호가 받을 수 있는 팁의 최댓값

for i in range(N):
    tip.append(int(input()))

tip.sort(reverse=True)      #팁 내림차순 정렬

for j in range(N):
    if (tip[j]-j > 0):      # tip[j] - ((j+1) - 1))              
        total += tip[j]-j

print(total)
