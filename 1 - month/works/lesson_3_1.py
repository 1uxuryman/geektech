# Циклы for, while

# c = 5
# while c != 0:
#     first = choice(numbers)
#     second = choice(numbers)
#     right_answer = first + second
#     student_answer = int(input(f"сколько будет {first} + {second}"))
#     c -= 1
#     if student_answer == right_answer:
#         print('правильно молодец')
#     else:
#         print(f'неправильно, {right_answer}')


# name = 'azat'
# print(name.index('z'))

# eng = 'aiyeou'
#
# while True:
#     vowels = 0
#     consonants = 0
#     user = input('Введите слово: ').lower()
#     if user == 'exit':
#         print('goodbye!')
#         break
#     for i in user:
#         if i in eng:
#             vowels += 1
#         else:
#             consonants += 1
#     print(f'гласные: {vowels}')
#     print(f'согласные: {consonants}')
#     print(f"гласные/согласные {round(vowels * 100 / len(user), 1)}% / "
#           f"{round(consonants * 100 / len(user), 1)}%")

# word = 'kyrgyzstan'

# c = 0
# while c != len(word):
#     print(word[c])
#     c += 1


# round = 5
# while round != 0:
#     print(round)
#     round = round - 1


# c = 0
# while c != 50:
#     c += 1
#     if c == 10:
#         continue
#     print('python  ', c)

# c = 0
# while 1:
#     c += 1
#     if c == 100:
#         continue
#     elif c == 150:
#         break
#     print('python  ', c)

# book_pages = 400
#
# point1, point2, point3 = 39, 117, 330
#
# for page in range(1, book_pages+1):
#     if page == point1 or page == point2 or page == point3:
#         print('мы нашли!')
#         continue
#         # break
#     print(page)

# for i in range(1, 6):
#     for k in range(1, 6):
#         print(i, k)

# for i in range(1, 6):
#     print(i)


# word = 'bishkek kyrgyzstan'
#
# print('q' in word)

#
# c = 1
# for letter in word:
    # if letter == 's':
    #     continue
    # if letter == 'h':
    #     print(letter.upper())
    # if letter == ' ':
    #     break
    # print(letter, c)
    # c += 1


# size = '44-42'
#
# if int(size[:2]) > int(size[3:]):
#     print('так не пойдет!')
# else:
#     print('пойдет!')
