# 맞아라 OX

# user_input = "OOXXOXXOOOO" (14)
# user_input = "OOXXOXXOOOXOXOXO" (13)

def solution(input):
    serial = 0
    total_score = 0
		
    for i in range(len(input)):
        if input[i]=='O':
            serial += 1
            total_score += serial
        else:
            serial = 0
            
    return total_score

if __name__=='__main__':
    input = input()
    if len(input)>1000:
        print("문제의 수는 1000을 넘을 수 없습니다")
        exit(1)

    print(solution(input))