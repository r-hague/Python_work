foo = 1
bar = 2
fibList = []

fibList.append(foo)
fibList.append(bar)

i = 0
while (foo < 4000000) and (bar < 4000000) and (i < 4000000):
    i = foo + bar
    if (i < 4000000):
        fibList.append(i)
    foo = bar + i
    if foo < 4000000:
        fibList.append(foo)
    bar = i + foo
    if bar < 4000000:
        fibList.append(bar)

mySum = 0
for fib in fibList:
    if fib % 2 == 0:
        mySum = mySum + fib

print fibList
print mySum


