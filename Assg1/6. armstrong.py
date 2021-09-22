def cubeSum(n):
    digits = 0
    t = n
    while t != 0:
        digits += 1
        t //= 10
    total = 0
    for i in range(digits):
        total += ((n % 10) ** digits)
        n //= 10
    return total

def isArmstrong(n):
    if n == cubeSum(n):
        return True
    return False

def printArmstrong(n):
    if isArmstrong(n):
        print("Armstrong")
    else:
        print("Not armstrong")


printArmstrong(153)
