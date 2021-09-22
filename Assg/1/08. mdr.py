def noDigits(n):
    digits = 0
    while n != 0:
        digits += 1
        n //= 10
    return digits

def MDR(n):
    while n // 10 != 0:
        digits = noDigits(n)
        prod = 1
        for i in range(digits):
            prod *= (n % 10)
            n //= 10
        n = prod
    return n


print(MDR(359))
