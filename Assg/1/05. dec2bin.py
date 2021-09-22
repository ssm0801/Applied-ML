n = int(input("Enter number = "))

# print(bin(n).replace('0b', ''))
s = ""
while n > 0:
    if n % 2 == 0:
        s += "0"
    else:
        s += "1"
    n //= 2

print(s[::-1])
