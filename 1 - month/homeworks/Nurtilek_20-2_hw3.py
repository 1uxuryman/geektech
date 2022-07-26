us = "qwertyuiop[]asdfghjkl;'zxcvbnm,.1234567890!@#$%^&*()_+"
ru = 'йцукенгшщзхъфывапролджэячсмитьбю1234567890!!"№%:,.;())_+'
while True:
    word = input("\nвведите слово:(для выхода нажмите 'q')\n").lower()
    if word == 'q':
        print("программа завершена")
        break
    for i in word:
        if i in us:
            Index1 = us.index(i)
            r = ru[Index1]
            print(r, end='')
        elif i in ru:
            index2 = ru.index(i)
            u = us[index2]
            print(u, end='')

