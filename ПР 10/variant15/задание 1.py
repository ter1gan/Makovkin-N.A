file = open(r"C:\Users\Nikito$\Desktop\variant15\Makovkin-N.A_Y-224_vvod1.txt",encoding='utf-8')
l = open(r"С:\Users\Nikito$\Desktop\variant15\Makovkin-N.A_Y-224_vvod1.txt",encoding='utf-8')
f = open(r"С:\Users\Nikito$\Desktop\variant15\Makovkin-N.A_Y-224_vivod1.txt", 'w+',encoding='utf-8')
R = l.readlines()
M = file.readlines(5)
N = file.readlines()
a = [int(x) for x in R]
b = [int(x) for x in M]
z = [int(x) for x in N]
def F(c,d):
    f.write('Номера строк:')
    for i in b:
        if i == c:
            f.write('0')
            break
    for i in z:
        if i == c:
            f.write('1')
            break
    f.write('\n')
    for i in a:
        if i == c:
            i *= d
            f.write(str(i))
        else:
            f.write(str(i))
    f.write('\n')
F(2,3)
f.close() 
    
                


