from imdb import Cinemagoer

print ("\nBem vindo!\n")

ia = Cinemagoer()

x = str (input("Digite o nome do filme:" " "))
y = 1
z = 0
while y == 1:
    movies = ia.search_movie(x)
    print(movies[z],"-","ID:", movies[z].movieID)
    z +=1

    if z == 20:
        b = int (input("\nDigite o ID do filme que deseja visualizar mais informações:" ""))
        movie = ia.get_movie(b)
        print("")
        print (movie,"\n")
        plot = movie['plot'][0]
        print (plot)
        print('\nDiretores:')
        for diretores in movie['directors']:
            print(diretores['name'])

        print ('\nGênero:')
        for genero in movie ['genres']:
            print(genero)



        a = str (input("\nDeseja procurar mais filmes? Digite 's' para sim e 'n' para não:" ""))
        if a == 's':
            z = 0
            x = str (input("\nDigite o nome do filme:" " "))
        else:
            y = 0
            print("\nObrigado por nos visitar!")
