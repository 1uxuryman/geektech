# Списки, Кортежи (list, tuple)
# from random import choice
#
# students = [2, 1, 6, 7, 4, 10, 16, 9]
# data = list()
#
# while len(students) != 0:
#     print(students)
#     id_student = choice(students)
#     name = input(f'Введите имя студента под {id_student} номером: ')
#     rate = int(input(f'ВВедите оценку для {name}: '))
#     if rate < 1 and rate > 5:
#         print("только от 1 до 5")
#         continue
#     data.append([name, rate])
#     students.remove(id_student)
#
# for i in data:
#     print(i)

# tpl = tuple(i for i in range(1, 11))
#
# new = tpl[:6]
# print(new)

# a = [1, True, 'ert']
#
# name = 'urmat'
# name = tuple(name)
#
# numbers = (3,)
# numbers += 2, 5, 6
#
# print(numbers)
# print(name)

# numbers = [i for i in range(1, 6)]
#
# objects = ['eagle', 'yellow', 'up']
# new = objects
#
#
# print(objects)
# print(new)

# print(objects == new)
# print(objects is new)

# objects.reverse()
# objects.sort(reverse=True)
# new = sorted(objects, key=len)
# print(objects)


# objects[1] = 3.5
# objects[-1], objects[2] = objects[2], objects[-1]



# objects.remove(11)
# del objects[1:4]
# del objects[1], objects[3]
# deleted = objects.pop(3)
# print(deleted)

# objects.append(123)
# objects.insert(0, 'word')
# objects.extend(numbers)
# objects += numbers

# print(type(objects))
# string1 = 'geektech'
# lst = list(string1)
# print(lst)


#
# for letter in objects:
#     print(letter)


# ['azat', 4]
# ['nursultan', 4]
# ['dastan', 4]
# ['urmat', 2]
# ['nurtilek', 6]
# ['baktybek', 5]
# ["el'man", 2]
# ['nazik', 2]
