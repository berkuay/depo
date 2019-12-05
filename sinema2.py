movie = {}
while True:
    movie_name=input("enter name of a movie ")
    if movie_name=="q":
        break
    else:
        imdb_rate = float(input("enter rate "))
        movie[movie_name] = imdb_rate
for name, score in movie.items():
    print(f"{name} movie has {score} rate ")
    """berkay"""
