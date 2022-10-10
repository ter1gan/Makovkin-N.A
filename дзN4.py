"# -- coding: utf-8 --"
a=int(input())           #1#
b=int(input())
while a <= b:
    print(a)
    a=a+1
a=int(input())           #2#
b=int(input())
while a < b:
    a=a+1
    print(a)
while a > b:
    a=a-1
    print(a)
a=int(input())           #3#
b=int(input())
while a > b:
    a = a-1
    if a % 2 == 1:
        print(a)
N = int(input())         #4#
sum = 0
for i in range(N):
    n = int(input())
    sum += n
print(sum)
n = int(input())          #5#         
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(sum)
n = int(input())          #6#
N = 1
for i in range(1, n + 1):
    N *= i
print(N)
n = int(input())          #7#
N = 1
sum = 0
for i in range(1, n + 1):
    N *= i
    sum += N
print(sum)
n = int(input())               #8#
for x in range(1, n + 1):
    for y in range(1, x + 1):
        print(y, end='')
    print()

    
 
    
    

    
        
    
    
    
    
              
