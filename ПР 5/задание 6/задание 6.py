n = int(input())
s = 0
k = 0
y = 0
while n != 0:
    k += 1
    s += n
    n = int(input())
    y = s // k
print(y)