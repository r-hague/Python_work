import string

alphaList = list(string.ascii_uppercase)

strPath = r"C:\Users\rhague\Documents\Tutorials\ProjectEuler\p022_names.txt"

str = open(strPath).read()
strNoQuote = str.replace('"', '')
nameList = strNoQuote.split(',')

sortedList = sorted(nameList)

rankNum = 1
runningScore = 0
for name in sortedList:
    nameScore = 0
    for letter in name:
        nameScore = nameScore + alphaList.index(letter) + 1
    nameScore = nameScore * rankNum
    runningScore = runningScore + nameScore
    rankNum += 1


print runningScore
