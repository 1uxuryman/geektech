movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },

    "Акыркы Сабак": {}
}

def find_element(movie_name):
    if not movie_name in movies:
        return True

def find_user_name(movie_name,user_name):
    if not user_name in movies[movie_name].keys():
        return True
    print("this username is already in use")

def add_movie(movie_name):
    if find_element(movie_name):
        movies[movie_name] = {}
        print(f'Movie {movie_name} added successfully')
    else:
        print("This movie already exist!")

def add_rate(movie_name, user_name, movie_rate):
    if not find_element(movie_name):
        movies[movie_name][user_name] = {movie_rate}
        print(f'A rating has been added for {movie_name}: {user_name} rated it {movie_rate}')
    else:
        print("netu takogo filma")

def show_ratings1():
    for i in movies:
        if len(movies[i].values()) > 0:
            average = round(sum(movies[i].values()) / len(movies[i].values()),1 )
            print(f"{i} is rated {average}")
        else:
            print(f"{i} is rated 0 ")
while True:
    print("comands: add - dobavit film\n"
          "rate - ocenit\n"
          "show - pokazat vse filmy")
    word = input("введите comandu:(для выхода нажмите 'q')\n").lower()
    if word == 'q':
        print("программа завершена")
        break
    elif word == "add":
        t = input("name of film")
        add_movie(t)
    elif word == "rate":
        a = input("name of film")
        b = input("your name ")
        c = input(f"your rate for {a}")
        add_rate(a,b,c)
    elif word ==("show"):
        show_ratings1()




