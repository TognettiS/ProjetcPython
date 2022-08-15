import random

def GeraNumeroAleatorio():
    global numeroaleatorio
    numeroaleatorio = random.randint(1,100)

def RecebeNumeroDoUsuario():
    global numerodigitado
    numerodigitado = int (input("\nDigite um número de 1 até 100: "))

def ConfereValores():
    y = 0
    while (y != 5):
        if numerodigitado == numeroaleatorio:
            print("\nAcertou!")
            break

        elif y == 4:
            print("\nVocê Perdeu!")
            break

        elif numerodigitado > numeroaleatorio:
            print("Valor muito alto")
            RecebeNumeroDoUsuario()
            y += 1
        elif numerodigitado < numeroaleatorio:
            print("Valor muito baixo")
            RecebeNumeroDoUsuario()
            y += 1

def MostraNumeroAleatorio():
    print(f"O Número era: {numeroaleatorio}")

print("Sorteador de números!\nVocê tem 5 tentativas para acertar o número. Boa Sorte!")
GeraNumeroAleatorio(), RecebeNumeroDoUsuario(), ConfereValores(), MostraNumeroAleatorio()
