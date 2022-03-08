#백준 12840번
#창용이의 시계

import sys

DAY = 60 * 60 * 24      #1일의 초

# 시간을 초로 변환
def to_second(h, m, s):
    seconds = 60 * 60 * h + 60 * m + s
    return seconds

# 초를 시간으로 변환
def to_time(sec):

    # 시간이 1일을 넘어가는 경우를 대비
    # DAY로 나눈 나머지만 사용
    sec %= DAY          
    
    hour = sec//3600
    minute = (sec%3600)//60
    second = (sec%3600)%60
    
    print(hour, minute, second)
    return


h, m, s = map(int, sys.stdin.readline().split())
sec = to_second(h, m, s)

for _ in range(int(sys.stdin.readline())):
    Tc = list(map(int, sys.stdin.readline().split()))

    if (Tc[0] == 1): sec += Tc[1]
    elif (Tc[0] == 2): sec -= Tc[1]
    else: to_time(sec)