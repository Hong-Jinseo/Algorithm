# 그리디
# 잃어버린 괄호

exp1 = list(input().split('-'))
exp2 = []

for e in exp1:
    temp = map(int, e.split('+'))
    exp2.append(sum(temp))

answer = exp2[0]
for e in exp2[1:]:
    answer -= e

print(answer)
