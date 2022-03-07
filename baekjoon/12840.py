#백준 12849번
#창용이의 시계

def to_second(h, m, s):
    seconds = 60 * 60 * h + 60 * m + s
    return seconds

def to_time(sec):
    print(sec//3600, (sec%3600)//60, (sec%3600)%60)
    return
        
h, m, s = map(int, input().split())
sec = to_second(h, m, s)

for _ in range(int(input())):
    Tc = list(map(int, input().split()))

    if (Tc[0] == 1): sec += Tc[1]
    elif (Tc[0] == 2): sec -= Tc[1]
    else: to_time(sec)