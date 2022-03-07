#백준 10818
#최소, 최대

n = int(input())
arr = input().split()

min = int(arr[0])
max = int(arr[0])
for i in range(n):
    num = int(arr[i])
    if(min > num):
        min = num
    if(max < num):
        max = num

print(min, max)
