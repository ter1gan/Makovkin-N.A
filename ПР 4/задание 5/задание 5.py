def F(n):
    sum = 0                   
    for i in range(1, n + 1):
        sum += i ** 3
    print(sum)
F(2)