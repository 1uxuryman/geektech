ten = [i for i in range(1,11)]
evens = list(filter(lambda x: x % 2 == 0, ten))
print(list(map(lambda x: x ** 2,evens)))
ind = (len(ten) - 1)
def print_index_obj(list = ten):
    while True:
        try:
            word = input("введите индекс :(для выхода нажмите 'q')\n").lower()
            if word == 'q':
                print("программа завершена")
                break
            else:
                word = int(word)
                print(ten[word])
        except IndexError:
            print("net takogo indexa")

print_index_obj()



