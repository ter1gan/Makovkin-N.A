x = [1,2,2,3,4,5,5]
s = set([i for i in x if x.count(i) > 1])
if len(s) > 0:
    print(*s)
else:
    print('отсутствуют')