# 구현
# 럭키 스트레이트

n = list(map(int, input()))
half = len(n)//2
first, second = n[:half], n[half:]

if sum(first) == sum(second):
    print('LUCKY')
else:
    print('READY')



