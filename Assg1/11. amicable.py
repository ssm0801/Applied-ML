def printAmicable(x, y):
    c = 1
    for i in range(x, y+1):
        if isAmicable(i) and i != sumPdivisors(i):
            c += 1
            if c % 2 == 0:
                print("({},{})".format(i, sumPdivisors(i)))

def isAmicable(n):
    if n == sumPdivisors(sumPdivisors(n)):
        return True
    return False

def sumPdivisors(n):
    sum_pd = 0
    for i in range(1, n):
        if n % i == 0:
            sum_pd += i
    return sum_pd


printAmicable(1, 7000)
