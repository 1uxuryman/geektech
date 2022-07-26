data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for x in data_tuple:
    if type(x) == str:
        letters.append(x)
    else:
        numbers.append(x)
del numbers[0]
letters.insert(8,numbers.pop(0))
numbers.insert(1,2)
numbers.sort()
letters.reverse()
letters[1] = "G"
letters[7] = "c"
numbers[0] = numbers[0] ** 2
numbers[1] = numbers[1] ** 2
numbers[2] = numbers[2] ** 2
numbers = tuple(numbers)
letters = tuple(letters)
print(letters)
print(numbers)
