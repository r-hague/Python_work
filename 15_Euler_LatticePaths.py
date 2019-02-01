pathArray = []

pathArray.append([1])
pathArray.append([1, 1])
pathArray.append([1, 2, 1])

latticeSize = 20

for i in range(2, latticeSize):
    nextTuple = [1]
    jMax = len(pathArray)-1
    for j in range(0, jMax):
        firstInt = pathArray[i][j]
        otherInt = pathArray[i][j+1]
        mySum = firstInt + otherInt
        nextTuple.append(mySum)
    nextTuple.append(1)
    pathArray.append(nextTuple)

for k in range(latticeSize, latticeSize*2):
    jMax = len(nextTuple) - 1
    j = 0
    nextTuple = []
    for j in range(0, jMax):
        firstInt = pathArray[k][j]
        otherInt = pathArray[k][j+1]
        mySum = firstInt + otherInt
        nextTuple.append(mySum)
    pathArray.append(nextTuple)

print pathArray[-1][-1]
