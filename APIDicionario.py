import requests
import json

def RecebePalavra():
    global palavrausuario
    palavrausuario = input("\nDigite a palavra que desejar: ")

def ProcuraSignificado():
    global palavrasignificado
    palavrasignificado = requests.get(f"https://significado.herokuapp.com/v2/{palavrausuario}")

def ProcuraSinonimo():
    global palavrasinonimo
    palavrasinonimo = requests.get(f"https://significado.herokuapp.com/v2/sinonimos/{palavrausuario}")

def TransformaEmJSON():
    global palavrasignificado, palavrasinonimo
    palavrasignificado, palavrasinonimo = palavrasignificado.json(), palavrasinonimo.json()

def MostrarSignificado():
    print("\nSignificados:\n")

    for i in range(len(palavrasignificado)):
        print(f"{palavrasignificado[i]}\n")

def MostrarSinonimo():
    print("Sinonimos:\n")
    print(f"{palavrasinonimo}\n")

def ProcurarNovamente():
    global respostausuario
    respostausuario = input("Digite 'S' caso queira procurar outra palavra, caso contrário digite qualquer valor.\n")

def Iniciar():
    y = 0
    while y == 0:
        RecebePalavra(), ProcuraSignificado(), ProcuraSinonimo(), TransformaEmJSON(), MostrarSignificado(), MostrarSinonimo(), ProcurarNovamente()
        if respostausuario == 'S' or respostausuario == 's':
            pass
        else:
            y = y + 1
            print("Obrigado!")

Iniciar()
