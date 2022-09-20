def sqnum(x):
    return x*x

def checkRightAngle(l1, l2, l3):
    if (sqnum(l1) + sqnum(l2)) ==  sqnum(l3):
        return 'right'
    elif (sqnum(l1) + sqnum(l3)) ==  sqnum(l2):
        return 'right'
    elif (sqnum(l2) + sqnum(l3)) ==  sqnum(l1):
        return 'right'
    else:
        return 'wrong'

while True:
    l1, l2, l3  = sorted(map(int, input().split()))
    if l1!=0:
        print(checkRightAngle(l1, l2, l3))
    else:
        break