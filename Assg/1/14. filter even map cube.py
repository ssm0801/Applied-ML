def even(n):
    if n % 2 == 0:
        return True
    return False

def cube(n):
    return n**3

def filterOddMapCube(l):
    # l = list(filter(lambda x: True if (x % 2 == 0) else False, l))
    l = list(filter(even, l))
    # l = list(map(lambda x: x**3, l))
    l = list(map(cube, l))
    return l


print(filterOddMapCube([1, 2, 3, 4, 5, 6]))
