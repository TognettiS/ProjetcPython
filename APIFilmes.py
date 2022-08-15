from imdb import Cinemagoer

bibliotecafilmes = Cinemagoer()

def Iniciar():
    RecebeNomeFilme(), ProcuraFilme(), RecebeIDdoFilme(), ExibeInformacoesDoFilme(), ProcurarDeNovo()

def RecebeNomeFilme():
    global nomefilme
    nomefilme = str (input("Digite o nome do filme:\n"))

def ProcuraFilme():
    pegafilmes = bibliotecafilmes.search_movie(nomefilme)
    print("\nSegue lista de filmes e IDs: \n")

    z = 0
    while z < 20:
        print(pegafilmes[z],"-","ID:", pegafilmes[z].movieID)
        z = z + 1

def RecebeIDdoFilme():
    global filme
    idfilme = int (input("\nDigite o ID do filme que deseja visualizar mais informações:\n"))
    filme = bibliotecafilmes.get_movie(idfilme)

def ExibeInformacoesDoFilme():
    print(f"\nNome do Filme: {filme}\n")

    historia = filme['plot'][0]
    if historia != None:
        print(f"História: {historia}")
    else:
        pass

    diretores = filme['directors']
    print('Diretores: ', end = '')
    for diretores in filme['directors']:
        print(diretores['name'])

    genero = filme['genres']
    print ('Gêneros: ', end = '')
    for genero in filme['genres']:
        print(genero, end = ' ')

def ProcurarDeNovo():
    maisfilmes = str (input("\n\nDeseja procurar mais filmes? Digite 's' para sim e 'n' para não:\n"))
    if maisfilmes == 'S' or maisfilmes == 's':
        Iniciar()
    else:
        print("\nObrigado pela visita!")

print ("\nBem vindo!\n")
Iniciar()
