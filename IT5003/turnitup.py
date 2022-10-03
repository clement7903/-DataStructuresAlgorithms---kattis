numOfRequests = int(input())
VOLUME = 7

for _ in range(numOfRequests):
    userRequest = input()
    if userRequest == 'Skru op!' and VOLUME < 10:
        VOLUME += 1
    elif userRequest == 'Skru ned!' and VOLUME > 0:
        VOLUME -= 1
    else:
        pass
print(VOLUME)