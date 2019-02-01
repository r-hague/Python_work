rangeA = range(1, 1001)
rangeB = range(1, 1001)

for a in rangeA:
    for b in rangeB:
        c = 1000 - a - b
        LS = (a**2) + (b**2)
        RS = c**2
        if LS == RS:
            product = a*b*c
            print "a is ", a, "b is ", b, "c is ", c
            print "Product is ", product
            quit()
