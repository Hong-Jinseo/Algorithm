# 정렬
# 국영수

n = int(input())
students = []
for _ in range(n):
    students.append(list(input().split()))

result = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for std in result:
    print(std[0])