"# -- coding: utf-8 --"
print('Курс Основы программирования начался')                                              #1#
a = 16823 * 12302 / 3092                                                                   #2#
print(a)                                                                
age = int(input('Укажите свой возраст: '))                                                 #3#
if age >= 16 and age < 75:
    print('Поздравляем вы поступили в ВГУИТ')
elif age > 0 and age < 16:
    print('Сначала нужно окончить школу!')
else:
    print('Введите возраст коректно')
name = str(input('Укажите свое имя: '))                                                   
if name == ('Иван'):
    print('Ваше имя не подходит')
if age < 16:
    print('Вам осталось учиться в школе ',16-age,'лет')
sekonds = int(input("Введите кол-во секунд "))                                            #4#
min = sekonds//60
hours = min//60
days = hours//24
print(days, ":" , hours, ":", min, ":", sekonds )
n = int(input('''Укажите число для решения выражения n + n^2 + n^3 + n^4 + n^5: '''))     #5#
print(n + n**2 + n**3 + n**4 + n**5)
a = 2                                                                                     #6#
b = 1
a, b = b, a
print(a)
print(b)
number = int(input())                                                                      #7#
if number % 2 == 0:
    print('Четное число')
else:
    print('Нечетное число')
