natRange = range(1, 101)
sumSquare = 0
mySum = 0

for natNum in natRange:
    sumSquare = sumSquare + natNum**2
    mySum = mySum + natNum
print "Sum of squares is ", sumSquare
squareSum = mySum**2
print "Square of sums is ", squareSum
myDiff = squareSum - sumSquare

print "Difference is ", myDiff

