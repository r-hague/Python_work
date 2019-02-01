fibList = [1, 1]
myStr = "1"
i = 2
while len(myStr) < 1000:
    fibList.append(fibList[i-1] + fibList[i-2])
    myStr = str(fibList[i])
    i += 1

print i



