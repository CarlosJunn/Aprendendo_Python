def decimalToBinary(decNumber):
    s = stack()

    while deNumber > 0:
        rem = decNumber % 2
        s.push(rem)

        decNumber = decNumber // 2
    binString = ''
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString