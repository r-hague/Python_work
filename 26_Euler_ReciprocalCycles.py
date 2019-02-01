from decimal import Decimal


def repeats(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string) % len(substring)]) == string:
            print(substring)
            return "break"

    print(string)


# for z in range(2, 1000):
#     y = Decimal(1.0 / z)
#     s = str(y)
#     t = repeats(s)
#     print t

print len(repeats("14285711428571142857114285711428"))
