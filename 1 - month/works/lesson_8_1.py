students = [6, 8, 9, 4, 1, 2, 3]

data = {
    'azat':  9,
    "nursultan":  8,
    "dastan": 11,
    "urmat": 4,
    "nurtilek": 13,
    "baktybek": 10,
    "el'man": 4,
    "nazik": 5,
    "reina": 5,
    "kylymbek": 2
}

while len(students) != 0:
    try:
        id_s = int(input('id student: '))
        name = input('name student: ')
        rate = int(input('rate student: '))
        if name in data.keys():
            data[name] += rate
            with open('students.txt', 'a') as file:
                file.write(f"{name} => {data[name]}\n")
        else:
            data[name] = rate
            with open('students.txt', 'a') as file:
                file.write(f"{name} => {data[name]}\n")
        students.remove(id_s)
    except:
        print('вводите только числа!')






# file = open('results.txt', 'w')
# file.write('geektech KG')
# file.close()

# with open('new_file.txt', 'a') as file:
#     file.write('\nБишкек, 996')

# with open('new_file.txt', 'r') as file:
#     for i in file.read():
#         time.sleep(0.3)
#         print(i, end='')

    # print(file.read())
