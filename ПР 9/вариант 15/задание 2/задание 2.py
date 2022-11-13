R = ([127,21,7],[1,2,7],[4,2,8])
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


  


    

            
            


                              
            

