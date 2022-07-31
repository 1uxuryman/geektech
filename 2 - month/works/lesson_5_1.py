# Первые три комманды пишутся только один раз когда вы делаете первый пуш
# git --version
# git config --global user.name "YOUR USERNAME ON GITHUB"
# git config --global user.email "YOUR EMAIL ON GITHUB"
#
# *
# git init
# git add .
# git status
# git commit -m "First Commit"
# git remote add origin <HTTPS link.git> - Remote тоже пишется единожды когда соединяем проект с репозиторем
# git branch
# git push -u origin master
#
# Когда вы все сделаете в след раз можете начинать с комманды
# git add .
# git status  (проверка нашего стэйжа)
# git commit -m "commit"
# git branch  (проверка на какой мы ветке)
# git push -u origin master
#
# потом скопируете мне ссылку вашего репозитория и отправите эту ссылку мне в личку телеграмма



import calculator
# from calculator import *
from person import Person
from random import randint as generate_number
from datetime import datetime, date

from termcolor import colored, cprint

import os

from decouple import config

# print(calculator.addition(12, 12))

# p1 = Person("Emir", 18)
# print(p1)

# print(generate_number(1, 100))

# yesterday = datetime(2022, 7, 18).date()
# today = date.today()
#
# day = datetime.strptime("23.03.2022", "%d.%m.%Y")

# print(datetime.now() - day)

# https://www.w3schools.com/python/python_datetime.asp
# https://pypi.org/


# text = colored('Hello, World!', 'green', attrs=['bold'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red', attrs=['bold'])

# print(os.environ.get("SECRET_KEY"))

# user = config("USER", default="anonim")
# passw = config("PASSWORD")
#
# print(user)
# print(passw, type(passw))