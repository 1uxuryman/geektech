# Введение в Python: Встроенные функции, переменные, комментарии.
# Базовые типы данных: строки, целые и дробные числа.
# str - это строка
# int - это целое число
# float - это дробное число

sum_ages = 30 + 21 + 17 + 23 + 21 + 36 + 17 + 26 + 16 + 27 + 15 + 16 + 19 + \
           19 + 22 + 21
print(sum_ages)

average_age_students = sum_ages / 16
average_age_students1 = round(average_age_students, 3)
average_age_students2 = '%.2f' % average_age_students

print(type(average_age_students1))
print(type(average_age_students2))

print('%.3f' % average_age_students)

# a = '8'
# b = '4'
# print((a + b) * 3)

# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)

# print(4 ** 3)
# print(5 % 2)
# print(20 // 7)

# name = input('ваше имя? ')
# surname = "o'neil"
# age = int(input('ваш возраст: '))
# height = 1.80
# year = 2022
#
# print(f'{name.title()} на земле с {year - age} года!')

# print(name, surname)
# print(name + ' ' + surname)
# print('{} {}'.format(name, surname))


# print(type(name))
# print(type(age))
# print(type(height))


# как можно создавать переменные
# var = 1
# var1 = 1
# Var = 1  # нежелательно
# _var = 1
# var_one = 1
# varOne = 1

# как нельзя создавать переменные
# 1var = 0
# v&ar$% = 0


# print('Hello, World!')
# print(2022)  # нынешний год
#print(2.5
