import math

#list leap years
leapList = []
nDays = 0
for i in range(1901, 2001):
    nDays += 365
    if i % 4 == 0:
        if (i % 100 == 0) and (i % 400 != 0):
            continue
        else:
            nDays += 1
            leapList.append(i)

FOM = []
m = 1
year = 1901

while year <= 2000:
    # Jan
    m += 31
    FOM.append(m)

    if year in leapList:
        #Feb NL
        m += 29
        FOM.append(m)
    else:
        #Feb L
        m += 28
        FOM.append(m)

    #Mar
    m += 31
    FOM.append(m)

    #Apr
    m += 30
    FOM.append(m)

    #May
    m += 31
    FOM.append(m)

    #Jun
    m += 30
    FOM.append(m)

    #Jul
    m += 31
    FOM.append(m)

    #Aug
    m += 31
    FOM.append(m)

    #Sep
    m += 30
    FOM.append(m)

    #Oct
    m += 31
    FOM.append(m)

    #Nov
    m += 30
    FOM.append(m)

    #Dec
    m += 31
    FOM.append(m)

    year += 1

FOMsundays = 0
for m in range(5, nDays, 7):
    if m in FOM:
        FOMsundays += 1

print FOMsundays


