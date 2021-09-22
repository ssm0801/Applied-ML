def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def twinprimes(n):
    for i in range(3, n-2, 2):
        if isprime(i) and isprime(i+2):
            print("({},{})".format(i, i+2))


print(twinprimes(1000))
