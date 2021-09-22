def even(n):
    if n % 2 == 0:
        return True
    return False

def removeOdd(l):
    l = list(filter(even, l))
    return l


print(removeOdd([4, 8, 3, 8, 2, 4, 79, 35, 8, 6, 98, 4, 54, 46, 57, 9854, 89, 7]))
