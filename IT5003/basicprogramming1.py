userInput = input().split()
N = int(userInput[0])
t = int(userInput[1])
A = list(map(lambda x : int(x)  , list(input().split())))

def t_1():
    return 7

def t_2():
    if A[0] > A[1]:
        return 'Bigger'
    elif A[0] == A[1]:
        return 'Equal'
    else:
        return 'Smaller'

def t_3():
    lst = [A[0], A[1], A[2]]
    lst = sorted(lst)
    return lst[1]

def t_4():
    return sum(A)

def t_5():
    even_userArray = list(filter(lambda x: (x%2==0), A))
    return sum(even_userArray)

def t_6():
    new_userArray = list(map(lambda x: x%26, A))
    chr_str = 'abcdefghijklmnopqrstuvwyxz'
    return ''.join(chr_str[i] for i in new_userArray)

def t_7():
    running_index = 0
    visited_index = {running_index}
    running_index = A[running_index]

    while running_index not in visited_index:
        if running_index not in range(0, N-1):
            return 'Out'
        elif running_index == N-1:
            return 'Done'
        visited_index.add(running_index)
        running_index = A[running_index]
    return 'Cyclic'

t_mapping = {
    1: t_1(), 
    2: t_2(),
    3: t_3(),
    4: t_4(),
    5: t_5(),
    6: t_6(),
    7: t_7()
}

print(t_mapping[t])