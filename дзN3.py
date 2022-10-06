"# -- coding: utf-8 --"
def add(x,y,z):                          #1#
    return x+y+z
print(add(7,8,9))
def add(a,b):                            #2#
    return 1/2 * a*b
print(add(5,4))
def F(n):                                #3#
    hours = n % (60 * 24) // 60
    minutes = n % 60
    print(hours, ":", minutes)
print(F(3245233))
def F(a, b, l, N):                       #4#
    return a + (2*N*a) + (2*b*N) + l
print(F(5, 3, 5, 4))
def F(a, b, c):                          #5#
    if a > b and c > b:
        print(b)
    if b > a and c > a:
        print(a)
    if b > c and a > c:
        print(c)
print(F(2,7,-1))
def f(a,b,c,d):                          #6#
    if a % 2 == 0 and b % 2 == 0:
        if c % 2 == 0 and d % 2 == 0:    
            print('Да')
    if a % 2 == 1 and b % 2 == 1:
        if c % 2 == 1 and d % 2 == 1:
            print('Да')
    if a % 2 == 0 and b % 2 == 0:
        if c % 2 == 1 and d % 2 == 1:
            print('Да')
    if a % 2 == 1 and b % 2 == 1:
        if c % 2 == 0 and d % 2 == 0:
            print('Да')
    if a % 2 == 0 and b % 2 ==1:
        if c % 2 == 0 and d % 2 == 0:
            print('Нет')
    if a % 2 == 1 and b % 2 ==0:
        if c % 2 == 0 and d % 2 == 0:
            print('Нет')
    if a % 2 == 0 and b % 2 ==0:
        if c % 2 == 1 and d % 2 == 0:
            print('Нет')
    if a % 2 == 0 and b % 2 ==0:
        if c % 2 == 0 and d % 2 == 1:
            print('Нет')
    if a % 2 == 1 and b % 2 ==0:
        if c % 2 == 1 and d % 2 == 1:
            print('Нет')
    if a % 2 == 0 and b % 2 ==1:
        if c % 2 == 1 and d % 2 == 1:
            print('Нет')
    if a % 2 == 1 and b % 2 ==1:
        if c % 2 == 0 and d % 2 == 1:
            print('Нет')
    if a % 2 == 1 and b % 2 ==1:
        if c % 2 == 1 and d % 2 == 0:
            print('Нет')
    if a % 2 == 1 and b % 2 == 0:
        if c % 2 == 1 and d % 2 == 0:
            print('Да')
    if a % 2 == 0 and b % 2 == 1:
        if c % 2 == 0 and d % 2 == 1:
            print('Да')
    if a % 2 == 1 and b % 2 == 0:
        if c % 2 == 0 and d % 2 == 1:
            print('Да')
    if a % 2 == 0 and b % 2 == 1:
        if c % 2 == 1 and d % 2 == 0:
            print('Да')
print(f(5,3,7,4))
def F(x):                                    #7#
    if x//4==0 and x//100!=0 and x//400!=0:
        print("Да")
    else:
        print("Нет")        
print(F(2000))
def F(a, b, c):                              #8#
    if a == b == c:
        return 3
    if a == b or b==c or c==a:
        return 2
    else:
        return 0
print(F(13, 13, 78))
def F(n,m,k):                                #9#
    if m*n//k:
        print("Да")
    else:
        print("Нет")
print(F(1,4,5))

    


    

