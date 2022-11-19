def F(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print("Да")
    else:
        print("Нет")
F(2000)