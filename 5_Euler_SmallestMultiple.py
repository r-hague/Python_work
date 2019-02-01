factorRange = range(11, 20)
multiple = 40
maxMultiple = (11*12*13*14*15*16*17*18*19*20)

while multiple <= maxMultiple:
    modSum = 0
    for factor in factorRange:
        if modSum != 0:
            break
        elif factor != 19:
            modSum = modSum + (multiple % factor)
        else:
            if multiple % factor == 0:
                print multiple
                quit()
    multiple += 20
