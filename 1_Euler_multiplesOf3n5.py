myList = []
i = 0
while i < 1000:
    myList.append(i)
    i += 3

j = 0
while j < 1000:
    if j not in myList:
        myList.append(j)
    j += 5

mySum = 0
for foo in myList:
    mySum = mySum + foo

print myList
print mySum
