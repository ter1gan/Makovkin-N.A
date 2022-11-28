from random import randint
def R(R):
    M = []
    for i in range(3):
        for j in range(3):
            if R[i][j] % 2 == 1:
                s = sum(R[i])
                M.append(s)
    for i in range(3):
        if sum(R[i]) == max(M):
            print('Номер строки:',i)
            break
    print('Сумма строки:', max(M))
R(([randint(0,9) for i in range(10)],[randint(0,9) for i in range(7)],[randint(0,9) for i in range(5)]))