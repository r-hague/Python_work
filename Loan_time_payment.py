import math

myFunc = input("Press 1 to calculate payment amount for a given duration and principal. \n Press 2 to calculate duration for a given payment amount and principal. \n Press 3 to calculate principal for a given duration and payment amount: ")

interestRate = input("Interest rate (%): ")
r = interestRate / 1200

if myFunc == 1:
    loanValue = input("Principal ($): ")
    duration = input("Loan duration (months): ")
    payment1 = (r*loanValue)/(1-((1+r)**(-1*duration)))
    payment = int(math.ceil(payment1))
    print "Monthly payment is $", payment
    totalPaid = payment*duration
    totalInterest = totalPaid-loanValue
    print "Total paid is $", totalPaid, " and the interest paid is $", totalInterest
    print "month interest balance"


elif myFunc == 2:
    loanValue = input("Principal ($): ")
    payment = input("Loan payment ($): ")
    duration1 = (-1*math.log(1-((r*loanValue)/payment)))/(math.log(1+r))
    duration2 = int(math.ceil(duration1))
    dur_yr = float(duration2)/12
    print "Loan duration is ", duration2, " months or ", dur_yr, " years "
    totalPaid = payment*duration2
    totalInterest = totalPaid-loanValue
    print "Total paid is $", totalPaid, " and the interest paid is $", totalInterest
    print "month interest balance"

elif myFunc == 3:
    payment1 = input("Loan payment ($): ")
    duration = input("Loan duration (months): ")
    loanValue1 = payment1*((1-(1+r)**(-1*duration))/r)
    loanValue = int(math.ceil(loanValue1))
    print "Loan principal is $", loanValue
    payment = int(math.ceil(payment1))
    totalPaid = payment * duration
    totalInterest = totalPaid - loanValue
    print "Total paid is $", totalPaid, " and the interest paid is $", totalInterest
    print "month interest balance"


else:
    print "error"

loanBalance = loanValue
i = 1
while loanBalance > 0.01:
    interest = (interestRate/1200)*loanBalance
    loanBalance = (interest + loanBalance) - payment
    print i, interest, loanBalance
    i += 1



