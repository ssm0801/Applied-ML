n = int(input("Enter number = "))

while n % 2 == 0:
    print(2, end=', ')
    n /= 2

div = 3
while n != 1 and div <= n:
    if n % div == 0:
        print(div, end=', ')
        n /= div
    else:
        div += 2


