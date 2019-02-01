def countSubHundred(tens, ones):
    nLet = 0
    if tens == '1':
        if ones in ['1', '2']:
            nLet += 6
        elif ones in ['5', '6']:
            nLet += 7
        elif ones in ['3', '4', '8', '9']:
            nLet += 8
        elif ones == '7':
            nLet += 9
        else:
            nLet += 3

    else:
        if tens in ['4', '5', '6']:
            nLet += 5
        elif tens in ['2', '3', '8', '9']:
            nLet += 6
        elif tens == '7':
            nLet += 7
        else:
            nLet += 0

        if ones in ['1', '2', '6']:
            nLet += 3
        elif ones in ['4', '5', '9']:
            nLet += 4
        elif ones in ['3', '7', '8']:
            nLet += 5
    return nLet;


myTotal = 0

for i in range(1, 1001):
    numString = str(i)
    if i == 1000:
        myCount = 11
    elif i >= 100:
        myCount = 10
        if i in range(100, 1000, 100):
            myCount = 7
        if numString[0] in ['1', '2', '6']:
            myCount += 3
        elif numString[0] in ['4', '5', '9']:
            myCount += 4
        elif numString[0] in ['3', '7', '8']:
            myCount += 5

        myCount = myCount + countSubHundred(numString[-2], numString[-1])

    elif i >= 10:
        myCount = countSubHundred(numString[-2], numString[-1])

    else:
        myCount = countSubHundred('0', numString[-1])
    print i, myCount
    myTotal = myTotal + myCount

print myTotal




