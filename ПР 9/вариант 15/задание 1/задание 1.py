def F(c,d,R):
    k = 0
    print('Номера строк:')
    for i in range(2):
        for j in range(3):
            if R[i].count(c) > 0:
                print(i, end=' ')
                break
    print()
    for i in range(2):
        for j in range(3):
            if R[i][j] == c:
                R[i][j] *= d
                print(R[i][j], end=' ')
            else:
                print(R[i][j], end=' ')
        print()
F(2,3,([2,2,4],[2,2,3])) 
                
  






            

                
    
        
    
    
        
        

        
        


