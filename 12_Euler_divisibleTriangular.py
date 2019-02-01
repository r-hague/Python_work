import math

j = 1
t = 1
factorCount = 2
while factorCount < 500:
    j += 1
    k = 2
    t = t + j
    factorCount = 2
    while k <= math.sqrt(t):
        if t % k == 0:
            if k == math.sqrt(t):
                factorCount += 1
            else:
                factorCount += 2
        k += 1

print t, "has", factorCount, "factors"


