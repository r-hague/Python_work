maxCollLen = 0

for j in range(1, 1000000):
    n = j
    collLen = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        collLen = collLen + 1
    if collLen > maxCollLen:
        maxCollLen = collLen
        maxCollStart = j

print maxCollStart

