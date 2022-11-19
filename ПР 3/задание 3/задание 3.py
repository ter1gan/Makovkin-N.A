def F(n):
    hours = n % (60 * 24) // 60
    minutes = n % 60
    print(hours, ":", minutes)
F(3458656)
