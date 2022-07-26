# dictionary, set (dict)
# {key: value}

# new1 = {1: 'one', 2: 'two'}
# new = dict(one=1, two=2)
#
# print(new1)
# print(new)

# numbers = 20, 50, 100
# names = 'togolok moldo', 'kurmanjan datka', 'toktogul satylganov'
#
# cash_dictionary = {}
#
# c = 0
# while c != len(numbers):
#     cash_dictionary[numbers[c]] = names[c]
#     c += 1
#
# for number, name in cash_dictionary.items():
#     print(f"{number} - {name}")
#
# print(cash_dictionary)


# menu = {
#     'plov': {'rice', 'meat', 'carrot'},
#     'beshbarmak': {'meat', 'noodles', 'onion'},
#     'shakarap': {'tomatoes', 'onion'},
#     'kurut': {'milk', 'salt'}
# }
#
# while True:
#     user = input('ingridient: ')
#     for k, v in menu.items():
#         if user in v:
#             print(k)
#     else:
#         print("doesn't exist")
#         ingridiennts = []
#         for i in menu.values():
#             ingridiennts += i
#         ingridiennts = set(ingridiennts)
#         for i in ingridiennts:
#             print(i)
#         # print(ingridiennts)





# plov = {'rice', 'meat', 'carrot'}
# beshbarmak = {'meat', 'noodles', 'onion'}
#
# print(plov.difference(beshbarmak))
# print(plov - beshbarmak)
#
# print(plov.union(beshbarmak))
# print(plov | beshbarmak)
#
# print(plov.intersection(beshbarmak))
# print(plov & beshbarmak)
#
# print(plov.symmetric_difference(beshbarmak))
# print(plov ^ beshbarmak)

# numbers = [1, 2, 3, 2, 2, 3, 4, 5, 5]
# numbers1 = {1, 2, 3, 2, 2, 3, 4, 5, 5}
#
# print(numbers)
# print(numbers1)


# student1 = {'name': 'Mark', 'height': 185}
# student.update(student1)

# numbers = [(1, 2), (3, 4)]
# numbers = dict(numbers)
# print(numbers)

# student = {
#     'name': 'Victor',
#     'age': 46,
#     'hobby': ['programming', 'reading', 'football'],
#     'married': False,
#     'smoke': True
# }
#
# for k, v in student.items():
#     print(v, '=>', k)



# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())




# del student['smoke']
# deleted = student.pop('hobby')
# print(deleted)
# # del student['hobby'][1]
# student['surname'] = 'Valdes'
# print(student)

# student['age'] = 40




# print(type(student))


# student = {
#     'name': 'Victor',
#     'age': 93,
#     2: 'two',
#     3.5: 'sedfs',
#     (1, 2, 3): 'werw',
#     True: 'sdfsd'
# }