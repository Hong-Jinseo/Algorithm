# 큰 수의 법칙
# 주어진 N개의 수를 M번 더하여 가장 큰 수를 만들되, 특정 인덱스의 수는 K번을 초과해서 연속으로 사용될 수 없다

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

# 내림차순 정렬
numbers.sort()
n1 = numbers[-1]     # 첫 번째로 큰 값
n2 = numbers[-2]     # 두 번째로 큰 값
result = 0

# "큰 수 k번, 작은 수 1번"을 한 세트로 볼 때, 몇 세트 연산 가능한지 계산
cnt = m//(k+1)
result += (n1 * k + n2) * cnt   # 한세트 * cnt번
result += n1 * (m % (k+1))

print(result)