def G(n):
    z = []
    for i in n:
        if i % 2 == 1:
            z.insert(0, i)   
    print('полученный массив: ',z)
    if len(z) == 0:
        print('таких чисел нет')
G([1,3,7,2,4,8])
        
      
     

    


    
    



    