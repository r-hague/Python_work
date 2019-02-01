import math
myRange = range(1, 10000)
mySet = myRange

amicableSum = 0

for foo in myRange:
    i = 2
    j = 2
    bar = 1
    barSum = 1
    if foo in mySet:
        while i <= math.sqrt(foo):
            if i == math.sqrt(foo):
                bar = bar + i
            elif foo % i == 0:
                bar = bar + i + (foo/i)
            i += 1

        if foo != bar:
            while j <= math.sqrt(bar):
                if j == math.sqrt(bar):
                    barSum = barSum + j
                elif bar % j == 0:
                    barSum = barSum + j + (bar/j)
                j += 1

            if barSum == foo:
                amicableSum = amicableSum + foo + bar
                mySet.remove(bar)
                print foo, bar

print amicableSum



