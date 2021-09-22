def prodDigits(n):
    prod = 1
    while n != 0:
        prod *= (n % 10)
        n //= 10
    return prod


print(prodDigits(12345))
