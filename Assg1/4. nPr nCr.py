n, r = list(map(int, input("Enter n and r = ").split()))

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


nPr = fact(n) / fact(n-r)
nCr = nPr / fact(r)

print("nPr = {}, nCr = {}".format(nPr, nCr))
