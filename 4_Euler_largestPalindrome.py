product = 997799
# i = 999
r = range(100, 1000)

while (product >= 10000):
    NumAsString = str(product)
    ReverseNum = NumAsString[::-1]
    if NumAsString == ReverseNum:
        for i in r:
            MyQuotient = product / i
            if (product % i == 0) and (MyQuotient in r):
                print "The largest palindrome is ", product
                product = 0
                break
    product -= 1
