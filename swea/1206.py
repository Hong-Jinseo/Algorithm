# View

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    height = list(map(int, input().split()))

    answer = 0

    for i in range(2, n-2):
        neighbor = max(height[i-2], height[i-1], height[i+1], height[i+2])
        if height[i] > neighbor:
            answer += height[i] - neighbor

    print("#{} {}".format(test_case, answer))
