import math

j = 1
t = 1
factorCount = 2
while factorCount < 90:
    j += 1
    k = 2
    t = t + j
    factorCount = 2
    while k <= math.sqrt(t):
        if (k < math.floor(math.sqrt(t))) and (t % k == 0):
            factorCount = factorCount + 2
            if k == math.sqrt(t):
                factorCount = factorCount - 1
        k += 1

print t, "has", factorCount, "factors"


