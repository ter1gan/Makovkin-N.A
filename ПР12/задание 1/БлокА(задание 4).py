def F(n, t):
    if n == 0:  
        return t
    else:
        return F(n-1, (t+(n)))
print(F(6, 0))

        

























    
