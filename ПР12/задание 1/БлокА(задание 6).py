def F(n):
    for i in range(2, n):
        if n % i == 1:
            return 'YES'
        else:
            return 'NO'
print(F(5))

    
