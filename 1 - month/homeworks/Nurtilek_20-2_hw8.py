min = 0
max = 100
med = 50
c = 0
user_number = input("number:")
while not(user_number.isdigit()):
    user_number = input("only numbers, number:")
with open("results.txt", 'w',) as number:
    number.write(f"attempts:")
    while True:
        print(f"number is {med}?")
        print("yes or < , >:")
        number.write(f"{med}")
        answer = input()
        c += 1
        if answer == '>':
            min = med
            med = (min + max) // 2
        elif answer == '<':
            max = med
            med = (min + max) // 2
        elif answer.lower() == 'yes':
            number.write(f'\nnumber of attempts: {c}')
            break
        else:
            print("yes or < , >")
        number.write(f"\nnumber: {med}")
