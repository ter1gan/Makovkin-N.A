def palindrom(n):
    spisok = []
    k = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            spisok.append(i)
        else:
            k = 0
    for i in spisok:                 
        if i <= n:
            a = bin(i)[2:]
            b = bin(i)[2:][::-1]                 
            if a == b:
                print(i, end=' ')                                
palindrom(400)
