# 그리디
# 잃어버린 괄호

# 덧셈 할 숫자들 묶기
exp = input().split('-')

sub = []
for e in exp:
    # 덧셈 수행
    temp = e.split('+')
    sub.append(sum(map(int, temp)))

# 뺄셈 수행
answer = sub[0]
for s in sub[1:]:
    answer -= s

print(answer)
