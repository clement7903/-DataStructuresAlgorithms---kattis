user_input = input().split()
method = user_input[0]
msg = user_input[1]

def encode(msg):
    encoded = ''
    current_letter = ''
    count = 0
    for letter in msg:
        if letter != current_letter:
            if current_letter != '':
                encoded += (current_letter + str(count))
            current_letter = letter
            count = 1
            continue
        count += 1
    encoded += (current_letter + str(count))
    return encoded

def decode(msg):
    output = ''
    num = 1
    if len(msg) == 1:
        return msg * num

    for char in msg:
        if char.isnumeric() == False:
            alpha = char
            continue
        else:
            num = int(char)
        output += alpha * num
    return output

if method == 'E':
    print(encode(msg))
else:
    print(decode(msg))