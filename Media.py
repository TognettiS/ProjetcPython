def RecebeNotas():
    print("Por favor digite suas 3 notas para calcular a média\n")
    y, notas = 1, []

    while y <= 3:
            inputusuario = input(f"Digite a {y}ª nota: ")
            notas.append(float(inputusuario))
            y += 1
    CalculaMedia(notas)

def CalculaMedia(notas):
    y, media = 0, 0

    while y < 3:
        media = media + notas[y]
        y += 1

    media = media / 3
    print("\nA sua média é:", round(media, 1))

RecebeNotas()
