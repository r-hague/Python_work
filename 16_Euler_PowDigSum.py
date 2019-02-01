powerValue = str(2 ** 1000)
mySum = 0

for myDigit in range(0, len(powerValue)):
    mySum = mySum + int(powerValue[myDigit])

print mySum