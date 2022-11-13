def D(a, b):
    d = 0
    for i in range(3):
        d += pow((a[i]-b[i]),2)
    return d 
I=['X','Y','Z','T']
s=[]
for i in range(4):
    b=[]
    print("Координаты точки:",I[i])
    for j in range(3):
        b.append(int(input()))
    s.append(b) 
f = True
for i in range(3):
    for j in range(i + 1, 4):
        r = D(s[i],s[j])
        if f or minr > r:
            m1=i
            m2=j
            minr = r
            f = False
print(F'Минимальное R между точками ',I[m1] , 'и' ,I[m2])
print(F'R между ними =', minr**0.5)
