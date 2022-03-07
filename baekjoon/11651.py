#백준 11651번
#좌표 정렬하기 2

coord = [] #좌표를 저장할 리스트

for _ in range(int(input())):
    x, y = map(int, input().split())
    coord.append((x, y)) #입력받은 좌표값을 튜플 형식으로 리스트에 저장

coord.sort(key=lambda z : (z[1], z[0]))
# key : 정렬 기준
# 정렬 1순위 기준 : y좌표 기준으로 오름차순
# 정렬 2순위 기준 : x좌표 기준으로 오름차순

for i in coord:
    print(i[0], i[1]) #튜플에 속한 값 출력