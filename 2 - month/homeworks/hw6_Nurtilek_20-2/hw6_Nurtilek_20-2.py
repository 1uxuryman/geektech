import re

while 1:

    user = int(input('1 = ФИО, 2 = email, 3 = файлы, 4 = цвета, 5 = выход :'))
    if user == 1:
        with open('MOCK_DATA.txt', 'r', encoding="utf-8") as file:
            content = file.read()
            with open('ФИО', 'w', encoding="utf-8") as fio:
                fio_list = re.findall(r"(?:[A-Z-'][a-z-']+\s)(?:[A-Za-z'-]*\s|[A-Za-z-'])", content)
                for i in fio_list:
                    i = str(i)
                    fio.write(i+'\n')
            print(fio_list)
    elif user == 2:
        with open("EMAIL", 'w', encoding='utf-8') as emails:
            email = re.findall(r"(?:[A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(?:\.[A-Z|a-z]{2,})+", content)
            for i in email:
                i = str(i)
                emails.write(i + '\n')
        print(email)
    elif user == 3:
        with open("File", 'w', encoding='utf-8') as files:
            file = re.findall(r'\s[A-Za-z]+\.[A-Za-z0-9]+', content)
            for i in file:
                i = str(i)
                files.write(i + '\n')
        print(file)
    elif user == 4:
        with open("Color", 'w', encoding='utf-8') as colors:
            color = re.findall(r'#[a-z0-9]+', content)
            for i in color:
                colors.write(i + '\n')
        print(color)
    elif user == 5:
        print('Выход')
        break
    else:
        print('только 1-5')

