film = {}
while True:
    film_ismi=input("film ismi giriniz")
    if film_ismi=="q":
        break
    else:
        imdb_puani= float(input("imdb puanı giriniz"))
        film[film_ismi] = imdb_puani
for name, score in film.items():
    print(f"{name} filminin puani {score}")
