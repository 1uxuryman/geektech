# Логический тип данных, условные конструкции и операторы.
# and, or, not
# bool - логический тип данных
from random import sample

from turtle import *
color('blue', 'pink')
begin_fill()
while True:
    forward(250)
    left(230)
    if abs(pos()) < 1:
        break
end_fill()
done()


# alphabet = 'qwertyuiopasdfghjklzxcvbnm'
# alphabetUpper = alphabet.upper()
# number = '123456789'
# symbols = '!@#$%^&*()+'
# data = alphabet + alphabetUpper + number + symbols
#
# password = sample(data, 8)
# print(data)
# print(str(password))
#
# print(alphabet)
# print(alphabetUpper)

# age = 18
# health = True
# family = 'жапаркулов'
#
# if 18 <= age <= 27 and health and family != 'жапаров':
#     print('goden!')
# else:
#     print('НЕ годен')

# signal = 'гаишник'
#
# if signal == 'red':
#     print('stop')
# elif signal == 'yellow':
#     print('wait')
# elif signal == 'green':
#     print('go')
# else:
#     print('look at sitution!')
#     if signal == 'гаишник':
#         print("слушаем гаишника!")
#     elif signal == 'главная дорога':
#         print("едем, но смотрим по сторонам")

password = input('введите пароль! ')
if len(password) >= 6 and not password.isalpha()\
        and not password.isdigit():
    print('ok')
    password1 = input('подтвердите: ')
    if password == password1:
        print('принято!')
else:
    print('no')


# print(type(True))
# print(bool(0))
# print(bool(0.0))
# print(bool(''))
# print(bool('asd'))
# print(bool(0.001))

# a = 'abc'
# print('x' in a)

# print(a is b)

# [start:end:step]

# password = '123456789'
# print(password[::-1])
# a = password[0:3]
# print(int(a) + 7)

# print(password.isdigit())
# print(password.endswith('b'))


# a = 14
# b = 6

# a = a + b
# a -= b
#
# print(a)

# print(2 == 3)
# print(2 > 3)
# print(2 < 3)
# print(2 <= 3)
# print(2 != 2)
# print(2 < 3 or 2 == 3)
# print(3 > 2 and 2 > 1)
# print(1 < 2 < 4)

# print('Hello, world!')

# time = input('введите время дня: ').lower()
#
# if time == 'утро' or time == 'morning':
#     print('доброе утро')
#
# elif time == 'день' or time == 'day':
#     print("добрый день!")
#
# elif time == "вечер"or time == 'evening':
#     print("добрый вечер")
#
# else:
#     print('Здраствуйте')
