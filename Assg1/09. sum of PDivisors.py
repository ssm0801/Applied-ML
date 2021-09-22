def sumPdivisors(n):
    sum_pd = 0
    for i in range(1, n):
        if n % i == 0:
            sum_pd += i
    return sum_pd


print(sumPdivisors(1210))
