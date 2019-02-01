import math
#28123


def abundant(n):
    mySum = 1
    t = math.sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0:
            mySum += i + (n / i)
        if t == int(t):
            mySum -= t
    if mySum > n:
        return True
    else:
        return False


limit = 28124
abn = set()
notSum = set()

for n in range(1, limit):
    if abundant(n) is True:
        abn.add(n)

    if not any((n-a in abn) for a in abn):
        notSum.add(n)
        print n

print len(abn), max(abn)
print len(notSum), max(notSum)

finalSum = sum(notSum)

print finalSum
