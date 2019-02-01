myInput = 100

myFactorial = 1
for i in range(1, myInput):
    myFactorial = myFactorial * i

factorialStr = str(myFactorial)

digitNum = 0
stringSum = 0

for digitStr in factorialStr:
    digitNum = int(digitStr)
    stringSum = stringSum + digitNum

print stringSum
