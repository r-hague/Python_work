import math

def isPrime ( i ):
    if i == 1:
        primeBool = False
    elif i < 4:
        primeBool = True
    elif i % 2 == 0:
        primeBool = False
    elif i < 9:
        primeBool = True
    elif i % 3 == 0:
        primeBool = False
    else:
        r = math.floor(math.sqrt(i))
        f = 5
        while f <= r:
            if i % f == 0:
                primeBool = False
                return primeBool;
            elif i % (f+2) == 0:
                primeBool = False
                return primeBool;
            f = f+6
        primeBool = True
    return primeBool;


primeSum = 2
j = 3
while j < 2000000:
    if isPrime(j) == True:
        primeSum = primeSum + j
    j += 1

print primeSum