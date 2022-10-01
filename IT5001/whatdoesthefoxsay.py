numofcases = input()

for _ in range(int(numofcases)):
    d_soundmadebyothers = []

    soundmadebyfox = input().split(' ')
    

    soundmadebyothers = ''
    while True:
        soundmadebyothers = input().split(' ')
        if soundmadebyothers == ['what', 'does', 'the', 'fox', 'say?']:
            break

        d_soundmadebyothers.append(soundmadebyothers[2])

        soundmadebyfox = filter(lambda a: a not in d_soundmadebyothers, soundmadebyfox)
        
    print(' '.join(soundmadebyfox))