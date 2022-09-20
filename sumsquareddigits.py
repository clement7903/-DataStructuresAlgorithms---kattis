num_cases = int(input())

def sumsqdigits(n):
    total = 0
    for integer in n:
        total += int(integer)**2
    return total
    
case_num = 0
    
for case in range(num_cases):
    user_input = input().split(' ')
    case_num += 1
    b = int(user_input[1])
    n = (user_input[2])
    
    print(f'{case_num} {sumsqdigits(n)}')
