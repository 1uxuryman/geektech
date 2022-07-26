date = input('Napishite datu\nv formate: "31/12":')
a = int(date[0:2:1])
b = int(date[3:])
if a <= 31 and b <= 12:
    if (a >= 21 and b == 3) or (a <= 19 and b ==4):
        print("oven")
    elif (a >= 20 and b == 4) or (a <= 20 and b ==5):
        print("telec")
    elif (a >= 21 and b == 5) or (a <= 21 and b ==6):
        print("bliznecy")
    elif (a >= 22 and b == 6) or (a <= 22 and b == 7):
        print("rak")
    elif (a >= 23 and b == 7) or (a <= 22 and b ==8):
        print("lev")
    elif (a >= 23 and b == 8) or (a <= 22 and b ==9):
        print("deva")
    elif (a >= 23 and b == 9) or (a <= 23 and b ==10):
        print("vesy")
    elif (a >= 24 and b == 10) or (a <= 22 and b == 11):
        print("scorpion")
    elif (a >= 23 and b == 11) or (a <= 21 and b ==12):
        print("strelec")
    elif (a >= 22 and b == 12) or (a <= 20 and b ==1):
        print("kozerog")
    elif (a >= 21 and b == 1) or (a <= 18 and b ==2):
        print("vodoley")
    elif (a >= 19 and b == 2) or (a <= 20 and b ==3):
        print("ryby")
else:
    print("ne pravilno vveli")