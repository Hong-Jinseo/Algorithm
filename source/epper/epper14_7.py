#깨알나라 신문 기사
"""
[입력]          [출력]
2 1 2 4         aaaa
a               aaaa
b               bbbb
b               bbb

[입력]          [출력]
2 3 1 3         aaabbbccc
abc             111222333
123
"""


#(행 개수, 열 개수, 행 반복 횟수, 열 반복 횟수, 입력값)
def solution(r, c, zr, zc, words):
    answer = [] #출력될 내용 가로 한 줄 씩 저장

    #행
    for i in range(r):
        row = ""
        #열
        for j in range(c):
            #열 필요한 만큼 반복
            for k in range(zc):
                row += words[i][j]
        #'필요한 만큼 반복한 열'을 필요한 만큼 반복해서 저장
        for l in range(zr):
            answer.append(row)
    
    return answer


r,c,zr,zc = input().split()
r=int(r)
c=int(c)
zr=int(zr)
zc=int(zc)

words=[]
	
for i in range(r):
    temp=input()
    if(len(temp)>c):
        print("입력 범위를 초과하였습니다.\n")
        exit(1)
    words.append(temp)

answer = solution(r,c,zr,zc,words);
  
for i in range(r*zr):
    print(answer[i])
