from random import randint
def F(c,d,R):
    k = 0
    print('Номера строк:')
    for i in range(2):
        for j in range(10):
            if R[i].count(c) > 0:
                print(i, end=' ')
                break
    print()
    for i in range(2):
        for j in range(10):
            if R[i][j] == c:
                R[i][j] *= d
                print(R[i][j], end=' ')
            else:
                print(R[i][j], end=' ')
        print()
F(2,3,([randint(0,9) for i in range(10)],[randint(0,9) for i in range(10)])) 