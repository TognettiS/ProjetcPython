import string

def IniciaisMaiusculas():
    for i in range(len(palavrasisoladas)):
        palavrasisoladas[i] = palavrasisoladas[i].capitalize()

def RetiraAcentuacao():
    for i in range(len(palavrasisoladas)):
        palavrasisoladas[i] = palavrasisoladas[i].translate(str.maketrans("","", string.punctuation))

def RetiraNumeros():
    for i in range(len(palavrasisoladas)):
        palavrasisoladas[i] = ''.join([i for i in palavrasisoladas[i] if not i.isdigit()])

def EncontraMaiorpalavra():
    maiorpalavra = max(palavrasisoladas, key = len)
    print(f"\nMaior palavra: {maiorpalavra}")

def TodasPalavrasSemPontuacao():
    todaspalavras = ' '
    todaspalavras = todaspalavras.join(palavrasisoladas).translate(str.maketrans("","", string.punctuation))
    print(f"Todas palavras: {todaspalavras}")

recebepalavras = input('Digite as palavras separando por espaço: ')
palavrasisoladas = recebepalavras.split()
IniciaisMaiusculas(), RetiraAcentuacao(), RetiraNumeros(), EncontraMaiorpalavra(), TodasPalavrasSemPontuacao()
