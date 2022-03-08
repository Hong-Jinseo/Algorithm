#백준 1946번
#신입사원

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    rank = []
    
    for _ in range(N):
        n, m = map(int, sys.stdin.readline().split())
        rank.append([n, m])

    rank.sort()             # 서류 등수 오름차순 정렬 (높은 등수부터)
    top_rank = rank[0][1]   # 서류 1등의 면접 등수 저장
    count = 1               # 합격자 수 (서류 1등은 합격 확정)

    # 기준값보다 서류등수는 낮은 사람 중 면접등수는 높은 사람 탐색
    for i in range(1, N):
        if top_rank > rank[i][1]:
            top_rank = rank[i][1]
            count+=1        # 합격자 수에 포함

    print(count)