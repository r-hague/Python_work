import math

#600851475143
bigNum = 600851475143

i = 2
j = 1
primeBool = False
while primeBool == False:
    while j != 0:
        i += 1
        j = bigNum % i
    factor = bigNum / i
    maxNumerator = math.floor(math.sqrt(factor))
    k = 2
    m = 1
    while (m != 0) and (k <= maxNumerator):
        k += 1
        m = factor % k
        if m == 0:
            primeBool = False
            j = 1
        else:
            primeBool = True

print factor
print "done"

