import math

i = 3
k = 1

while k < 10001:
    myMod = 1
    j = 2
    while j <= math.floor(math.sqrt(i)):
        myMod = myMod * (i % j)
        j += 1
    if myMod != 0:
        k += 1
    i += 2

print i - 2
