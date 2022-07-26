countries = {
    'kg': {'red', 'yellow'},
    'ru': {'red', 'white', 'blue'},
    'ua': {'blue','yellow'},
    'tr': {'red', 'white'},
    'de': {'black', 'yellow','red'},
    'kz': {'blue','yellow'}
}
while True:
    color = input("(для выхода нажмите 'q')\nцвет:").lower()
    if color == "q":
        print("bye <3")
        break
    for  k,v in countries.items():
       if set(color.split()) <= (v):
            print(k)
    else:
        print("doesn't exist")
        colors = list()
        for i in countries.values():
            colors += i
        colors = set(colors)
        for i in colors:
            print(i)