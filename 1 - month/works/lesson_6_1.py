# Функции, аргументы: *args, **kwargs.
# keyword arguments


numbers = [1,2,3]


def find_element(obj):
    if obj in numbers:
        return True
    print('НЕ нашли')


def add(obj):
    if not find_element(obj):
        numbers.append(obj)


def edit(obj, new_obj):
    if find_element(obj):
        numbers[numbers.index(obj)] = new_obj

# print(add(5))
edit(2, 22)
print(numbers)

# student = {
#     'name': 'aza',
#     'age': 20
# }
#
# # print(student['nam'])
# print(student.get('nam', 'нет такого ключа!'))

# def max_digit(number: int):
#     number = str(number)
#     return int(max(number))
#
#
# print(type(max_digit(52)))


# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False
#
# print(is_even(23))
# print(is_even(22))

# def lunch(**kwargs):
#     return kwargs
# print(lunch(drink='cola', eat='burger'))


# def plus(*args):
#     print(type(args))
#     return sum(args)
#
#
# print(plus())


# def greeting(name, age):
#     print(f'Hello, {name}, {age} лет')
#     # return f'Hello, {name}, {age} лет'
#
# new_str = greeting('rasul', 25)
# print(new_str)

# print(greeting(age=20, name='samat'))


# def get_square(width, length):
#     square = width * length
#     return square
#
#
# square_2_class = get_square(5, 7)
# square_3_class = get_square(4, 5)
# square_4_class = get_square(3, 4)
#
# # print((square_2_class + square_3_class + square_4_class) * kavrolin)
#
#
# def get_total_price(price, squares):
#     return sum(squares) * price
#
# kavrolin = 200
# squares = [square_2_class, square_3_class, square_4_class]
# print(squares)

# print(get_total_price(kavrolin, squares))



# width = 5
# length = 7
# square_2_class = width * length
# print(square_2_class)
#
#
# width = 4
# length = 5
# square_3_class = width * length
# print(square_3_class)
