def isPerfect(n):
    if n == sumPdivisors(n):
        return True
    return False

def sumPdivisors(n):
    sum_pd = 0
    for i in range(1, n):
        if n % i == 0:
            sum_pd += i
    return sum_pd

def printPerfectNo(n):
    for i in range(1, n+1):
        if isPerfect(i):
            print(i)


printPerfectNo(1000)
